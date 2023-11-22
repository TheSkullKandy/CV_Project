import cv2
import numpy as np
import streamlit as st

# Create a Streamlit app
st.title('Image Transformations')

uploaded_image = st.file_uploader("Upload an input image", type=["jpg", "jpeg", "png"])
if uploaded_image is not None:
    image = cv2.imdecode(np.frombuffer(uploaded_image.read(), np.uint8), cv2.IMREAD_COLOR)
else:
    st.write("Please upload an image as an input.")

transformation = st.sidebar.selectbox("Select Transformation for image", ["Original", "Translation", "Rotation", "Scaling", "Shearing"])

if uploaded_image is not None:
    if transformation == "Original":
        st.image(image, caption='Original Image', use_column_width=True, channels="BGR")
    else:
        if transformation == "Translation":
            translation_x = st.number_input("X Translation (pixels)", -500, 500, 50)
            translation_y = st.number_input("Y Translation (pixels)", -500, 500, 50)
            translation_matrix = np.float32([[1, 0, translation_x], [0, 1, translation_y]])
            transformed_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))
        elif transformation == "Rotation":
            rotation_angle = st.number_input("Rotation Angle (degrees)", -180, 180, 50)
            rotation_matrix = cv2.getRotationMatrix2D((image.shape[1] / 2, image.shape[0] / 2), rotation_angle, 1)
            transformed_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))
        elif transformation == "Scaling":
            scaling_x = st.number_input("X Scaling Factor", 0.1, 2.0, 1.5)
            scaling_y = st.number_input("Y Scaling Factor", 0.1, 2.0, 1.8)
            scaling_matrix = np.float32([[scaling_x, 0, 0], [0, scaling_y, 0]])
            transformed_image = cv2.warpAffine(image, scaling_matrix, (image.shape[1], image.shape[0]))
        elif transformation == "Shearing":
            shearing_x = st.number_input("X Shearing Factor", -1.0, 1.0, 0.6)
            shearing_y = st.number_input("Y Shearing Factor", -1.0, 1.0, 0.7)
            shearing_matrix = np.float32([[1, shearing_x, 0], [shearing_y, 1, 0]])
            transformed_image = cv2.warpAffine(image, shearing_matrix, (image.shape[1], image.shape[0]))
            
        
        st.image(transformed_image, caption=f'{transformation} Image', use_column_width=True, channels="BGR")
