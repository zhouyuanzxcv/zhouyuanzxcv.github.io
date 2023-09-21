---
title: "Medical Image Analysis"
collection: teaching
type: "Undergraduate Course"
permalink: /teaching/Medical Image Analysis
venue: "Fudan University, School of Data Science"
date: 2023-02-25
location: "Shanghai, China"
---

This course teaches the basics of medical image analysis. It mainly contains four parts: reconstruction, enhancement, segmentation and registration. The covered contents are focused on the classic methodology used in this area.  

# Contents

- **Chapter 1 Introduction**  
	- 1.1. Imaging Fundamentals  
		- XR, CT, MRI, PET/SPECT, Ultrasound  
	- 1.2. Problems  
		- Segmentation, Registration, Computer Aided Diagnosis, etc  
	- 1.3. Mathematical Preliminaries  
		- Continuous vs. discrete space  
		- Numerical schemes  
		- Information theory  
- **Chapter 2 Reconstruction**  
	- 2.1. Fourier Transform  
		- Complex number  
		- Fourier Transform 1D/2D and properties  
		- Convolution theorem  
	- 2.2. Sampling Theorem, DFT and FFT  
		- Sampling Theorem  
		- Discrete Fourier Transform  
		- Fast Fourier Transform  
	- 2.3. CT Reconstruction  
		- Radon transform  
		- Projection slice theorem  
		- Filtered backprojection  
- **Chapter 3 Enhancement**  
	- 3.1. Introduction and Filtering  
	- 3.2. Scale Space  
		- Heat equation  
		- Anisotropic diffusion  
	- 3.3. Calculus of Variations  
	- 3.4. From Local Filtering to Global Filtering  
		- Total variation denoising  
		- Bilateral filter  
		- Nonlocal means  
- **Chapter 4 Segmentation**  
	- 4.1. Segmentation Basics  
		- Region-based vs edge-based  
		- Edge detection   
		- Hough transform  
		- Dynamic programming  
	- 4.2. Snake  
		- Parametric curve  
		- Snake  
		- Gradient vector flow  
	- 4.3. Level set  
		- Implicit curve/surfaces and geometric properties  
		- Signed distance function  
		- Level set methods  
		- Constructing signed distance function  
		- Geodesic active contour  
		- Chan-Vese model  
	- 4.4. Shape prior  
		- Active shape model  
- **Chapter 5 Registration**  
	- 5.1. Introduction to registration  
		- Single modality vs multiple modality  
		- Transformations  
		- Similarity metric  
	- 5.2. Searching  
		- Multiresolution search strategy  
		- Phase correlation  
	- 5.3. Deformable registration  
		- Diffusion model  
		- Demon  
		- Changing the similarity metric  
	- 5.4. Diffeomorphic Registration  
		- Diffeomorphic Demon  
		- LDDMM  
		- SyN, DARTEL  
- **Chapter 6 Application**  
	- 6.1. Computer Aided Diagnosis  
		- Linear and nonlinear classifiers  
		- Interpretable machine learning  
	- 6.2. Disease Progression Model  
		- Voxel/deformation-based morphometry  
		- Event-based model  
		- Linear dynamical system  

# References

1. P. Suetens, "Fundamentals of Medical Imaging", Cambridge Univ. Press, 2017  
2. Rafael C. Gonzalez, Richard E. Woods, "Digital Image Processing", Fourth edition, Pearson Education International  
3. Joachim Weichert, "Anisotropic Diffusion in Image Processing", 1998  
4. Stanley Osher, Ronald Fedkiw, "Level Set Methods and Dynamic Implicit Surfaces", Springer  
5. Related papers