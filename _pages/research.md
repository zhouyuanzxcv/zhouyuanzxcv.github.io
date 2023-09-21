---
layout: archive
permalink: /research/
title: ""
---


<div class="features">
	<article>
		<div class="inner">
			<h2>Disease Progression Modeling</h2>
			<p style="text-align:justify; text-justify:inter-ideograph;">Disease progression models (DPM) aim to recover the trajectory of disease progression using a collection of short time series. A time series corresponds to multiple visits of a patient. At each visit, a patient is examined and various measurements (MRI, PET/SPECT, CSF, clinical scores) about the disease state are acquired. By combining these imaging/CSF/clinical biomarkers from all the patients, the disease progression trajectory can be retrieved. Our research is mainly focused on neurodegenerative diseases, such as Alzheimer's disease (AD), Parkinson's disease (PD) 
			(<a href="../files/papers/Du_Zhou_2023_Filtered Trajectory Recovery.pdf">IPMI 2023</a>, 
			<a href="../files/papers/Zhou et al_2021_Robust Bayesian analysis of early-stage Parkinson's disease progression using DaTscan images.pdf">TMI 2021</a>, 
			<a href="../files/papers/Zhou_Tagare_2019_Bayesian longitudinal modeling of early stage Parkinson's disease using DaTscan images.pdf">IPMI 2019</a>). </p>
		</div>
		<a href="#" class="image"><img src="/images/research/medical_imaging/AD_progression.jpg" alt="" /></a>
	</article>
	<article>
		<div class="inner">
			<h2>Interpretable Machine Learning</h2>
			<p style="text-align:justify; text-justify:inter-ideograph;">Computer aided diagnosis using deep learning can achieve very high accuracy in classifying disease from normals in medical images. However, without explaining which part in the image contributes to the decision, the results are unreliable in clinical practice. We use the Shapley value, saliency maps, and other interpretable network architectures to make interpretable deep learning in computer aided diagnoisis of AD, PD, ASD using MRI/SPECT/fMRI 
			(<a href="../files/papers/Zhang et al_2023_A-GCL.pdf">MedIA 2023</a>, 
			<a href="../files/papers/Zhang et al_2022_3D Global Fourier Network for Alzheimer's Disease Diagnosis Using Structural MRI.pdf">MICCAI 2022</a>, 
			<a href="../files/papers/Zhou_Tagare_2021_Self-normalized Classification of Parkinson's Disease DaTscan Images.pdf">BIBM 2021</a>, 
			<a href="../files/papers/Li et al_2021_BrainGNN.pdf">MedIA 2021</a>, 
			<a href="../files/papers/Li et al_2020_Pooling Regularized Graph Neural Network for fMRI Biomarker Analysis.pdf">MICCAI 2020</a>
			). </p>
		</div>
		<a href="#" class="image"><img src="/images/research/medical_imaging/gfnet_arch.jpg" alt="" /></a>
	</article>
	<article>
		<div class="inner">
			<h2>Medical Image Segmentation</h2>
			<p style="text-align:justify; text-justify:inter-ideograph;">Traditional medical image segmentation is achieved by handcrafted algorithms targeted to a specific region. Nowadays, segmentation is achieved by training based algorithms (such as U-Net) that treat segmentation as a pixel-wise classification problem. We apply contrastive learning in semi-supervised medical image segmentation 
			(<a href="../files/papers/You et al_2022_SimCVD.pdf">TMI 2022</a>). </p>
		</div>
		<a href="#" class="image"><img src="/images/research/medical_imaging/simcvd.jpg" alt="" /></a>
	</article>
	<article>
		<div class="inner">
			<h2>Multiband Image Registration/Fusion</h2>
			<p style="text-align:justify; text-justify:inter-ideograph;">A hyperspectral image has a low spatial resolution and a high spectral resolution. A multispectral image, on the contrary, has a high spatial resolution but a low spectral resolution. Fusing these two types of images can lead to a both spatially and spectrally high-resolution image. Before fusion, they need to be registered. We propose a simultaneous registration and fusion algorithm to combine these two types of images 
			(<a href="../files/papers/Zhou et al_2020_An Integrated Approach to Registration and Fusion of Hyperspectral and Multispectral Images.pdf">TGRS 2020</a>). </p>
		</div>
		<a href="#" class="image"><img src="/images/research/hyperspectral/reg_fusion_flowchart.jpg" alt="" /></a>
	</article>
	<article>
		<div class="inner">
			<h2>Hyperspectral Image Unmixing</h2>
			<p style="text-align:justify; text-justify:inter-ideograph;">Hyperspectral images, despite their high spectral resolution that can characterize different materials, have a low spatial resolution (e.g. 16m per pixel). Hence, a pixel in a hyperspectral image typically contains multiple materials. How to find the spectra of these materials and their proportions in a pixel --- a.k.a. hyperspectral unmixing --- is a core problem in hyperspectral image analysis. We propose a Gaussian mixture model to unmix hyperspectral images 
			(<a href="../files/papers/Zhou et al_2020_Unmixing urban hyperspectral imagery using probability distributions to represent endmember variability.pdf">RSE 2020</a>, 
			<a href="../files/papers/Zhou et al_2018_A Gaussian mixture model representation of endmember variability in hyperspectral unmixing.pdf">TIP 2018</a>, 
			<a href="../files/papers/Zhou et al_2016_A spatial compositional model for linear unmixing and endmember uncertainty estimation.pdf">TIP 2016</a>). </p>
		</div>
		<a href="#" class="image"><img src="/images/research/hyperspectral/mixed_pixel.jpg" alt="" /></a>
	</article>
</div>


<style>
.features article {
	border-top: solid 3px #f4f4f4;
	margin-bottom: 2.25em;
}

	.features article:first-child {
		border-top: 0;
		padding-top: 0;
	}

	.features article .image {
		display: inline-block;
		padding-left: 2.5em;
		vertical-align: middle;
		width: 48%;
	}

		.features article .image img {
			display: block;
			width: 100%;
		}

	.features article .inner {
		display: inline-block;
		vertical-align: middle;
		width: 50%;
	}

		.features article .inner > :last-child {
			margin-bottom: 0;
		}
</style}

