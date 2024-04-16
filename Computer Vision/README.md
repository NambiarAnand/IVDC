# Computer Vision (ML Based PS)
## Question 1
In computer vision, image filters act like specialized tools to enhance or manipulate images. These filters achieve various goals by applying mathematical operations to an image's pixels. There are two main categories: linear filters and non-linear filters. Linear filters, like the mean and Gaussian filters, work by averaging neighboring pixel values. This is good for noise reduction but can blur edges. Non-linear filters, like the median filter, are more complex and better suited for certain tasks like removing specific noise patterns while preserving sharpness.
Common filters have specific applications. Gaussian filters, with their balance of smoothing and edge keeping, are often the go-to choice for noise reduction. Sobel filters excel at highlighting edges, making them crucial for object recognition. Laplacian filters are another edge detection option but are more sensitive to noise. The choice of filter depends on the computer vision task at hand. For instance, reducing noise with a Gaussian filter before applying a Sobel filter can optimize edge detection in a noisy image. By understanding these filters and their impact, computer vision algorithms can effectively extract the most relevant information from images for tasks like object recognition and analysis.

## Question 2
Adaptive filters excel in image processing tasks like denoising and edge detection by cleverly adjusting to local image variations. Unlike fixed filters with a one-size-fits-all approach, adaptive filters analyze a pixel's neighborhood to understand noise level or edge presence. This allows them to tailor their filtering for each pixel. In noisy areas, they can apply stronger noise reduction, while preserving details in smoother regions. Similarly, they can adjust edge detection based on local contrast, avoiding the excessive blurring common with fixed filters. This adaptability translates to superior noise reduction, preserved edges, and more accurate feature extraction during image processing tasks. In essence, adaptive filters are like having a toolbox of specialized filters, automatically choosing the right tool for each pixel based on the image's local characteristics.

## Question 3
Convolutional neural networks (CNNs) rely on filter kernels, tiny trainable templates, to shift through images and extract valuable features. These kernels, often square matrices (consisting of weights), slide across the input image, performing element-wise multiplication with the underlying image data. During training, the network adjusts these weights to become sensitive to specific features crucial for the task.
Kernel size is another key factor. Smaller kernels excel at capturing low-level features like edges and corners. As we increase the kernel size, it can capture more complex features by combining these low-level building blocks. By stacking convolutional layers with varying kernel sizes, CNNs build a hierarchy of features, from basic shapes to intricate object parts.

## Question 4
Real-time computer vision filters require a balancing act between speed, accuracy, and adaptability. Complex filters may be accurate but slow down processing. Simple filters run fast but might lack precision. Ideally, filters should adapt to lighting changes and object motion, but complex adaptive filters can be slow. The key is to choose the right filter like mean filter for noise reduction and optimize its parameters like kernel size, stride and padding for the specific task. In some cases, hardware acceleration can handle more complex filters while maintaining real-time performance. Overall, thoughtful filter design is crucial for robust computer vision applications in dynamic environments.

## Question 5
Since the image is blurred/noisy, first we would try to denoise the image using filters like the Gaussian filter, because it is good at preserving the edges and denoises the image very well. Then to reduce the intensity of horizontal lines, directional filters like Sobel filters can be used when oriented in vertical direction, as it increases the intensity of edges in the vertical direction, significantly reducing the intensity of horizontal power lines. 
Another method is morphological filtering, where it shrinks and dilates the image. Apply it first to horizontal features, and then dilate the image, so that most of the features are restored but the powerlines.

## Question 6, 7
I have used the pretrained models available in keras.applications and have used the XCeption Model.

Other models which i have tried include:
>Resnet50 (good accuracy, high inference time) <br>
>Inception (average accuracy, high inference time) <br>
>MobileNet (lower accuracy, low inference time) <br>
>EfficientNetB6 (high accuray, high inference time)<br>

XCeption Model gives very high accuracy when compared to others (99.95%) in test data, with average inference time of about 30 minutes on CPU. I have trained the files locally. Jupyter Notebook has been attached
