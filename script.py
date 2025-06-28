import cv2
import numpy as np
import streamlit as st

# Function to process the images
def process_images(target, pattern):
    h, w = target.shape[:2]

    # Perspective warp
    src_pts = np.float32([[280, 90], [290, 650], [980, 810], [1030, 250]])
    dst_pts = np.float32([[0, 0], [pattern.shape[1], 0],
                          [pattern.shape[1], pattern.shape[0]], [0, pattern.shape[0]]])
    matrix = cv2.getPerspectiveTransform(dst_pts, src_pts)
    warped = cv2.warpPerspective(pattern, matrix, (w, h))

    # Alpha mask (with lighter feather)
    gray_warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray_warped, 1, 255, cv2.THRESH_BINARY)
    dist = cv2.distanceTransform(mask, cv2.DIST_L2, 5)
    alpha = cv2.normalize(dist, None, 0, 1.0, cv2.NORM_MINMAX)
    alpha = cv2.GaussianBlur(alpha, (15, 15), 0)  # smaller blur
    alpha = np.clip(alpha, 0, 1.0)

    # Fold deformation
    gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced = clahe.apply(gray)

    dx = cv2.Sobel(enhanced, cv2.CV_32F, 1, 0, ksize=3)
    dy = cv2.Sobel(enhanced, cv2.CV_32F, 0, 1, ksize=3)
    dx = cv2.GaussianBlur(dx, (7, 7), 0)
    dy = cv2.GaussianBlur(dy, (7, 7), 0)

    map_x, map_y = np.meshgrid(np.arange(w), np.arange(h))
    map_x = map_x.astype(np.float32) + 6 * dx / 255.0  # stronger displacement
    map_y = map_y.astype(np.float32) + 6 * dy / 255.0

    deformed = cv2.remap(warped, map_x, map_y, interpolation=cv2.INTER_LINEAR)

    # Shading adjustment
    luminance = cv2.GaussianBlur(enhanced, (25, 25), 0).astype(np.float32) / 255.0
    shading = np.clip(0.5 + 0.8 * luminance, 0.3, 1.3)
    shaded = np.clip(deformed.astype(np.float32) * shading[..., None], 0, 255)

    # Alpha blending (linear)
    flag_float = target.astype(np.float32)
    opacity = 0.92
    final = alpha[..., None] * shaded * opacity + (1 - alpha[..., None] * opacity) * flag_float
    final = np.clip(final, 0, 255).astype(np.uint8)

    return final


# Streamlit UI
st.title("Flag Mapping Project")

# === File upload for images ===
flag_file = st.file_uploader("Upload Flag Image", type=["png", "jpg", "jpeg"])
pattern_file = st.file_uploader("Upload Pattern Image", type=["png", "jpg", "jpeg"])

if flag_file and pattern_file:
    # Read the uploaded images
    target = cv2.imdecode(np.frombuffer(flag_file.read(), np.uint8), cv2.IMREAD_COLOR)
    pattern = cv2.imdecode(np.frombuffer(pattern_file.read(), np.uint8), cv2.IMREAD_COLOR)

    # Process the images
    final_image = process_images(target, pattern)

    # Display the final image in Streamlit
    st.image(final_image, channels="BGR", use_container_width=True)
else:
    st.warning("Please upload both flag and pattern images.")