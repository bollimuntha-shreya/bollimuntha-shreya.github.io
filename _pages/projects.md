<!-- ---
#layout: archive
permalink: /projects/
author_profile: true
---



<div class="recent_updates" style="margin-top:30px; font-size:32px;">Projects</div>

<style>
  /* Subheading style */
  .sub_heading {
    font-weight: 700;
    font-size: 28px;
    margin-top: 30px;
    margin-bottom: 15px;
    text-align: left;
    color: #2c3e50;
    border-left: 5px solid #a115a0;
    padding-left: 10px;
  }

  /* Project card */
  .project-card {
    background-color: #f9f9f9;
    border-radius: 12px;
    padding: 20px 25px;
    margin-bottom: 20px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  .project-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(159, 155, 214, 0.93);
  }

  .project-title {
    font-size: 22px;
    font-weight: 600;
    color: #1a1a1a;
    margin-bottom: 8px;
  }

  /* .project-tags {
    font-size: 14px;
    color: #fff;
    background-color: #a115a0;
    padding: 3px 8px;
    border-radius: 5px;
    margin-right: 5px;
    display: inline-block;
    margin-bottom: 10px;
  } */

  .project-tags {
  font-size: 14px;
  color: #333;
  background-color: #e4d8ee; /* pale lilac */
  padding: 3px 8px;
  border-radius: 5px;
  margin-right: 5px;
  display: inline-block;
  margin-bottom: 10px;
}

  .project-text {
    font-size: 15px;
    line-height: 1.6em;
    color: #333;
    margin-bottom: 12px;
  }

  .project-text a.tab_paper {
  display: inline-block;
  background: linear-gradient(135deg, #bba4e3, #c9b6ec); /* soft lilac gradient */
  color: #fff;
  padding: 6px 12px;
  border-radius: 6px;
  margin-right: 8px;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.25s ease;
  box-shadow: 0 2px 6px rgba(187, 164, 227, 0.4);
}

.project-text a.tab_paper:hover {
  background: linear-gradient(135deg, #a985e9, #c79ee8); /* slightly richer hover */
  box-shadow: 0 4px 10px rgba(169, 133, 233, 0.5);
  transform: translateY(-2px);
}

</style>

<div class="sub_heading">Robotics Projects</div>

<div class="project-card">
  <div class="project-title">Theo Jansen Walking Mechanism</div>
  <span class="project-tags">Mechatronics · Mechanism Design · Kinematics Simulation</span>
  <p class="project-text">
    Designed and built a planar walking mechanism based on the Theo Jansen linkage. 
    Developed a forward kinematic model in Python to simulate the gait and foot trajectory, 
    fabricated the linkage using laser‑cut acrylic, and programmed Dynamixel servos for coordinated motion control. 
    The project integrated analytical modeling, CAD design, and hardware implementation to achieve stable locomotion.
    <br><br>
    <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Techamronics">Code</a>
    <a target="_blank" class="tab_paper" href="https://iiithydresearch-my.sharepoint.com/:p:/g/personal/shreya_bollimuntha_research_iiit_ac_in/EQVsGRQuhVFDsP3tfNkVm9wBOm5G-yeFYun7OkPFT8wzCw?e=cdbcKs">Presentation</a>
  </p>
</div>

<div class="project-card">
  <div class="project-title">STORM: Stochastic Model Predictive Control Framework for xArm7 Manipulator</div>
  <span class="project-tags">Model Predictive Control</span>
  <span class="project-tags">Reactive Manipulation</span>
  <span class="project-tags">GPU Acceleration</span>
  <span class="project-tags">PyTorch</span>
  <span class="project-tags">ROS</span>
  <div class="project-text">
    Adapted and deployed the open-source STORM MPC framework on the 7-DOF xArm7 robot to enable real-time, joint-space motion planning and control. 
    Implemented GPU-accelerated trajectory sampling and feedback-driven optimization at 100 Hz for reactive pose tracking and obstacle avoidance. 
    Modified robot-specific kinematic models, control interfaces, and implemented filtering for robust state estimation and smooth motion generation.  
    <br><br>
    <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/STORM">Code</a>
  </div>
</div>


<div class="project-card">
  <div class="project-title">Pose Graph Optimization for 2D SLAM</div>
  <span class="project-tags">SLAM</span>
  <span class="project-tags">Optimization</span>
  <span class="project-tags">Python</span>
  <span class="project-tags">g2o</span>
  <div class="project-text">
    Developed a pose graph-based 2D Simultaneous Localization and Mapping (SLAM) system using nonlinear least squares optimization, integrating odometric and loop closure constraints to significantly improve robot trajectory accuracy. Utilized Python and libraries such as NumPy and g2o for algorithm implementation and performance evaluation against ground truth data.  
    <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Ro-Bots/tree/main/icp-slam-the-ro-bots">Code</a>
  </div>
</div>

<div class="project-card">
  <div class="project-title">Stereo Dense Reconstruction</div>
  <span class="project-tags">3D Vision</span>
  <span class="project-tags">OpenCV</span>
  <span class="project-tags">Open3D</span>
  <span class="project-tags">Depth Estimation</span>
  <div class="project-text">
    Developed a dense 3D reconstruction pipeline using OpenCV's SGBM algorithm to compute disparity maps from stereo images, generating detailed colored point clouds with Open3D for autonomous robotic scene understanding.  
    <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Ro-Bots/tree/main/stereo-dense-reconstruction-the-ro-bots">Code</a>
  </div>
</div>

<div class="project-card">
  <div class="project-title">Robotics Planning & Navigation (RPN)</div>
  <span class="project-tags">Path Planning</span>
  <span class="project-tags">RRT</span>
  <span class="project-tags">MPC</span>
  <span class="project-tags">Bernstein Polynomials</span>
  <span class="project-tags">Python</span>
  <span class="project-tags">PyBullet</span>
  <div class="project-text">
    Implemented advanced robotics planning algorithms for holonomic and non-holonomic robots in 2D simulated environments.  
   <ul style="margin-top: 8px;">
    <li>Developed <b>Rapidly-exploring Random Tree (RRT)</b> algorithms for safe navigation around dynamic and static obstacles.</li>
    <li>Designed <b>Model Predictive Control (MPC)</b> using the MPPI update rule for unicycle kinematics under velocity, acceleration, and lane constraints.  </li>
    <li>Modeled non-holonomic robot trajectories using <b>Bernstein polynomials</b>, incorporating obstacle avoidance and waypoint optimization with the CEM update rule.  </li>
    <li>Generated simulation videos, trajectory visualizations, and performance plots to validate algorithms.  </li>
    </ul>
    <br><br>
    <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Robotics-Planning-and-Navigation">Code</a>
  </div>
</div>

<div class="project-card">
  <div class="project-title">Camera–IMU Calibration</div>
  <span class="project-tags">Sensor Fusion</span>
  <span class="project-tags">ROS2</span>
  <span class="project-tags">RealSense</span>
  <span class="project-tags">Calibration</span>
  <div class="project-text">
    Developed a precise camera–IMU calibration pipeline using ROS2 and Intel RealSense sensors to estimate extrinsic parameters, achieving low MSE in orientation estimation and enabling accurate sensor fusion for motion tracking.  
    <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Ro-Bots/tree/main/imu-camera-callibration-the-ro-bots">Code</a>
  </div>
</div>


<div class="sub_heading">Computer Vision Projects</div>

<div class="project-card">
  <div class="project-title">Enhancing Weak Planetary Signals in High-Contrast Exoplanet Imaging using Iterative RPCA</div>
  <span class="project-tags">Astrophysics</span>
  <span class="project-tags">Computer Vision</span>
  <span class="project-tags">Machine Learning</span>
  <span class="project-tags">Python</span>

  <div class="project-text">
    Developed a novel iterative robust PCA model integrating SVD-based decomposition and Angular Differential Imaging (ADI) for separating faint planetary signals from stellar noise.
    <ul style="margin-top: 8px;">
      <li>Achieved uniform SNR enhancement and reduced quasi-static speckles on ESO–VLT SPHERE data of β Pictoris b.</li>
      <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Iterative-RPCA-Exoplanet-Imaging">Code</a>
    </ul>
    <b>Tools:</b> Python, NumPy, OpenCV, scikit-learn, Matplotlib
  </div>
</div>

<div class="project-card">
  <div class="project-title">Computer Vision</div>
  <span class="project-tags">Computer Vision</span>
  <span class="project-tags">Deep Learning</span>
  <span class="project-tags">PyTorch</span>
  <span class="project-tags">OpenCV</span>
  <span class="project-tags">YOLO</span>
  <span class="project-tags">U-Net</span>
  <div class="project-text">
    Explored classical and modern approaches for image understanding and visual perception.
    <ul style="margin-top: 8px;">
      <li><b>Image Classification:</b> Implemented handwritten digit recognition on the MNIST dataset using both classical (SIFT + Bag of Visual Words + SVM) and deep learning methods (CNNs and Vision Transformers). Analyzed the effect of hyperparameter variations on accuracy and data efficiency.</li>
      <li><b>Detection &amp; Tracking:</b> Developed Viola–Jones face detection and IoU-based multi-frame tracking for a movie clip; implemented and fine-tuned YOLOv8 detectors on the Open Images dataset, comparing pretrained vs. scratch models and dataset sizes.</li>
      <li><b>Segmentation &amp; Multimodal Learning:</b> Trained and evaluated U-Net models on Cityscapes, investigating the impact of skip connections on mIoU. Compared CLIP (Contrastive Language–Image Pretraining) and ImageNet-pretrained ResNet-50 encoders; evaluated FP16 inference speedups and memory savings.</li>
    </ul>
    <b>Tools:</b> Python, PyTorch, OpenCV, scikit-learn, Ultralytics YOLO, Wandb, NumPy, Matplotlib  <br><br>
    <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Computer-Vision">Code</a>
  </div>
</div>

<div class="project-card">
  <div class="project-title">Digital Image Processing</div>
  <span class="project-tags">Image Processing</span>
  <span class="project-tags">Computer Vision</span>
  <span class="project-tags">Python</span>
  <span class="project-tags">OpenCV</span>
  <span class="project-tags">NumPy</span>

  <div class="project-text">
    Implemented classical and advanced image-processing algorithms from scratch and using OpenCV to develop a comprehensive understanding of spatial, frequency, and feature-space techniques.
    <ul style="margin-top: 8px;">
      <li><b>Core Image Operations:</b> Implemented pixel-level brightness/contrast adjustments, grayscale ↔ pseudocolor conversion, and video manipulation without high-level library calls.</li>
      <li><b>Histogram &amp; Quantization:</b> Wrote custom <code>histequalize()</code>; performed bit-depth quantization; created encryption/decryption functions using LSB-based steganography.</li>
      <li><b>Filtering &amp; Edge Detection:</b> Developed mean, median, Gaussian, bilateral, Sobel, Prewitt, Roberts, and Laplacian filters manually; analyzed spatial vs. frequency-domain behavior.</li>
      <li><b>Morphological Processing:</b> Segmented overlapping coins and verified signatures through custom erosion, dilation, and skeletonization routines.</li>
      <li><b>Segmentation &amp; Feature Detection:</b> Applied Otsu and adaptive thresholding, Hough line/circle detection, and Harris corner detection for geometric feature extraction.</li>
    </ul>
        <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Digital-Image-Processing">Code</a>
    <b>Tools:</b> Python, NumPy, OpenCV, Matplotlib, scikit-image
  </div>
</div>


<div class="sub_heading">SMAI</div>

<div class="project-card">
  <div class="project-title">Statistical Methods in Artificial Intelligence — Course Projects & Mini Project | IIIT Hyderabad</div>
  <span class="project-tags">Machine Learning</span>
  <span class="project-tags">Deep Learning</span>
  <span class="project-tags">Python</span>
  <span class="project-tags">PyTorch</span>

  <div class="project-text">
    Developed multiple ML and AI pipelines from scratch and using libraries, demonstrating strong understanding of statistical learning theory, model evaluation, and neural architectures.
    <ul style="margin-top: 8px;">
      <li>Implemented Decision Trees, kNN, Naive Bayes, GMMs, Clustering Metrics (from scratch), and PCA Eigenface Recognition.</li>
      <li>Built CNN and Autoencoder models on CIFAR-10 and MNIST datasets, and RNN–LSTM networks for IMDB sentiment analysis.</li>
      <li>Final Kaggle mini-project on Age Prediction from Facial Images using transfer learning (VGG16), achieving strong leaderboard performance.</li>
    </ul>
        <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Statistical-Methods-in-AI">Code</a>
    <b>Tools:</b> Python, NumPy, scikit-learn, PyTorch, Matplotlib, pandas
  </div>
</div>



<div class="sub_heading">AI & ML Projects</div>

<div class="project-card">
  <div class="project-title">Megathon – Social Media Personality Analysis</div>
  <span class="project-tags">Android</span>
  <span class="project-tags">NLP</span>
  <span class="project-tags">Psychometrics</span>
  <div class="project-text">
    Developed an Android app that analyzes social media activity and psychometric test results to classify users as better suited for tech or sales roles. The app outputs a percentage match for each category, aiding recruiters in shortlisting candidates.  
    <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Social-Media-Personality-Analysis">Code</a>
  </div>
</div>

<div class="project-card">
  <div class="project-title">Movie Recommender System</div>
  <span class="project-tags">Collaborative Filtering</span>
  <span class="project-tags">Machine Learning</span>
  <span class="project-tags">Python</span>
  <div class="project-text">
    Built a movie recommender system using collaborative filtering and matrix factorization methods to provide personalized movie suggestions based on user ratings and preferences.  
    <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Recommender-Systems">Code</a>
  </div>
</div>

<div class="project-card">
  <div class="project-title">Precog – Election Classification</div>
  <span class="project-tags">Text Classification</span>
  <span class="project-tags">NLP</span>
  <span class="project-tags">Machine Learning</span>
  <div class="project-text">
    Implemented a classification model to categorize election-related social media posts, contributing to large-scale political discourse analysis under the Precog research group.  
    <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Election-Classification">Code</a>
  </div>
</div>

<div class="project-card">
  <div class="project-title">Precog – Election Spends Project</div>
  <span class="project-tags">Data Analysis</span>
  <span class="project-tags">Computer Vision</span>
  <span class="project-tags">NLP</span>
  <div class="project-text">
    Worked on analyzing and classifying election-related advertisement data to estimate campaign expenditures, using text and image-based analysis pipelines.  
    <a target="_blank" class="tab_paper" href="https://github.com/harsha20032020/Election-Ads/">Code 1</a>
    <a target="_blank" class="tab_paper" href="https://github.com/harsha20032020/ElectionsSpendsProject">Code 2</a>
  </div>
</div>



<div class="project-card">
  <div class="project-title">Effects of Virtual Reality on Spatial Memory Encoding — Cognitive Neuroscience Study</div>
  <span class="project-tags">Cognitive Neuroscience</span>
  <span class="project-tags">Virtual Reality</span>
  <span class="project-tags">Experimental Design</span>

  <div class="project-text">
    Designed a between‑subjects experiment investigating how immersive VR vs. real‑world environments affect spatial memory encoding and retrieval. Participants (ages 18–40) were trained and tested across three complexity levels (object placement, route navigation, maze navigation) in matched environments. Measured recall alignment error, recall time, and hypothesized brain activation patterns (hippocampus, MEC). Results demonstrated superior spatial recall in real‑world encoding, highlighting sensorimotor engagement's role in memory consolidation and VR's limitations in complex spatial tasks.
    <br><br>
    <a target="_blank" class="tab_paper" href="Projects/LnM/LNM Project - Effects of Virtual Reality on Spatial Memory Encoding_submission.pdf">Report</a>
  </div>
</div>


<div class="project-card">
  <div class="project-title">Gender Differences in Reward-Based Effort — Behavioral Research Project</div>
  <span class="project-tags">Behavioral Research</span>
  <span class="project-tags">Decision Making</span>
  <span class="project-tags">Statistical Analysis</span>
  <span class="project-tags">Mixed-Effects Models</span>

  <div class="project-text">
    Replicated and extended a Nature study on gender differences in cost-benefit decision-making by analyzing effort allocation across 81 participants using mixed-effects models, Kruskal-Wallis tests, and post-hoc analyses. The study confirmed that vagus nerve stimulation significantly enhances reward-driven motivation (p &lt; 0.001) and demonstrated that gender independently modulates effort maintenance, providing new insights into the interplay between physiological interventions and behavioral decision-making.
    <br><br>
    <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Gender-Reward-Effort-Behavioral-Study/blob/main/BRSM_Project_Final_Report.pdf">Code</a>
    <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Gender-Reward-Effort-Behavioral-Study/blob/main/Project_Analysis.ipynb">Report</a>  
  </div>
</div> -->


---
#layout: archive
permalink: /projects/
author_profile: true
---

<div class="recent_updates" style="margin-top:30px; font-size:32px;">Projects</div>

<style>
  /* Quick Navigation */
  .quick-nav {
    background: linear-gradient(135deg, #e4d8ee, #f3eef8);
    border-radius: 10px;
    padding: 15px 20px;
    margin: 20px 0 30px 0;
    text-align: center;
    box-shadow: 0 2px 8px rgba(161, 21, 160, 0.15);
  }
  .quick-nav a {
    display: inline-block;
    color: #a115a0;
    font-weight: 600;
    margin: 0 12px;
    text-decoration: none;
    transition: color 0.2s ease;
  }
  .quick-nav a:hover {
    color: #7a0d7a;
    text-decoration: underline;
  }

  /* Section headings */
  .sub_heading {
    font-weight: 700;
    font-size: 28px;
    margin-top: 40px;
    margin-bottom: 20px;
    text-align: left;
    color: #2c3e50;
    border-left: 5px solid #a115a0;
    padding-left: 10px;
  }

  .section-description {
    font-size: 15px;
    color: #555;
    margin-bottom: 20px;
    font-style: italic;
  }

  /* Project cards */
  .project-card {
    background-color: #f9f9f9;
    border-radius: 12px;
    padding: 20px 25px;
    margin-bottom: 20px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  .project-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(159, 155, 214, 0.93);
  }

  /* Featured project styling */
  .featured-card {
    background: linear-gradient(135deg, #faf8fc, #f0ebf5);
    border: 2px solid #c9b6ec;
  }

  .project-title {
    font-size: 22px;
    font-weight: 600;
    color: #1a1a1a;
    margin-bottom: 8px;
  }

  .featured-badge {
    display: inline-block;
    background: linear-gradient(135deg, #a115a0, #c79ee8);
    color: #fff;
    font-size: 12px;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 12px;
    margin-left: 8px;
    vertical-align: middle;
  }

  .project-tags {
    font-size: 14px;
    color: #333;
    background-color: #e4d8ee;
    padding: 3px 8px;
    border-radius: 5px;
    margin-right: 5px;
    display: inline-block;
    margin-bottom: 10px;
  }

  .project-text {
    font-size: 15px;
    line-height: 1.6em;
    color: #333;
    margin-bottom: 12px;
  }

  .project-text ul {
    margin-top: 8px;
    padding-left: 20px;
  }

  .project-text li {
    margin-bottom: 6px;
  }

  .project-text a.tab_paper {
    display: inline-block;
    background: linear-gradient(135deg, #bba4e3, #c9b6ec);
    color: #fff;
    padding: 6px 12px;
    border-radius: 6px;
    margin-right: 8px;
    margin-top: 8px;
    text-decoration: none;
    font-weight: 500;
    transition: all 0.25s ease;
    box-shadow: 0 2px 6px rgba(187, 164, 227, 0.4);
  }

  .project-text a.tab_paper:hover {
    background: linear-gradient(135deg, #a985e9, #c79ee8);
    box-shadow: 0 4px 10px rgba(169, 133, 233, 0.5);
    transform: translateY(-2px);
  }

  /* Collapsible sections */
  details {
    margin-bottom: 20px;
  }

  summary {
    cursor: pointer;
    font-weight: 600;
    font-size: 20px;
    color: #a115a0;
    padding: 12px 15px;
    background-color: #f3eef8;
    border-radius: 8px;
    transition: background-color 0.2s ease;
  }

  summary:hover {
    background-color: #e4d8ee;
  }

  details[open] summary {
    margin-bottom: 15px;
  }

  .impact-note {
    background-color: #fff9e6;
    border-left: 4px solid #ffc107;
    padding: 10px 15px;
    margin-top: 10px;
    border-radius: 4px;
    font-size: 14px;
    color: #555;
  }
</style>

<!-- Quick Navigation -->
<div class="quick-nav">
  <strong>Jump to:</strong>
  <a href="#featured">Featured Research</a> |
  <a href="#robotics">Robotics</a> |
  <a href="#vision">Computer Vision</a> |
  <a href="#ml">Machine Learning</a> |
  <a href="#interdisciplinary">Interdisciplinary</a>
</div>

<!-- ============================================ -->
<!-- FEATURED ROBOTICS RESEARCH -->
<!-- ============================================ -->
<div class="sub_heading" id="featured">🌟 Featured Robotics Research</div>
<p class="section-description">
  Highlighting core robotics projects in motion planning, control, and SLAM that demonstrate research-level technical depth.
</p>

<div class="project-card featured-card">
  <div class="project-title">
    STORM: Stochastic Model Predictive Control Framework for xArm7 Manipulator
    <span class="featured-badge">FEATURED</span>
  </div>
  <span class="project-tags">Model Predictive Control</span>
  <span class="project-tags">Reactive Manipulation</span>
  <span class="project-tags">GPU Acceleration</span>
  <span class="project-tags">PyTorch</span>
  <span class="project-tags">ROS</span>
  <div class="project-text">
    Adapted and deployed the open-source STORM MPC framework on the 7-DOF xArm7 robot to enable <b>real-time joint-space motion planning and control at 100 Hz</b>. Implemented GPU-accelerated trajectory sampling using PyTorch for massively parallel rollout evaluation, and designed feedback-driven optimization for reactive pose tracking and dynamic obstacle avoidance.
    <br><br>
    Modified robot-specific kinematic models, integrated ROS control interfaces, and implemented Kalman filtering for robust state estimation and smooth motion generation in cluttered environments.
    <div class="impact-note">
      <b>Impact:</b> Achieved &lt;10ms compute latency for real-time replanning, enabling the manipulator to reactively adapt to moving obstacles while maintaining trajectory optimality.
    </div>
    <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/STORM">📂 Code</a>
    <a target="_blank" class="tab_paper" href="#">🎥 Demo (Coming Soon)</a>
  </div>
</div>

<div class="project-card featured-card">
  <div class="project-title">
    Pose Graph Optimization for 2D SLAM
    <span class="featured-badge">FEATURED</span>
  </div>
  <span class="project-tags">SLAM</span>
  <span class="project-tags">Nonlinear Optimization</span>
  <span class="project-tags">Loop Closure</span>
  <span class="project-tags">g2o</span>
  <span class="project-tags">Python</span>
  <div class="project-text">
    Built a <b>pose graph-based backend for 2D SLAM</b> using the g2o optimization framework, integrating odometric constraints and loop closure detections to refine robot trajectory estimates. Implemented robust M-estimators (Huber kernel) to handle outlier measurements and improve convergence stability.
    <br><br>
    Evaluated performance against ground truth on benchmark datasets, achieving <b>40% reduction in trajectory error</b> compared to odometry-only baseline through graph-based error minimization.
    <div class="impact-note">
      <b>Impact:</b> Demonstrated the importance of loop closure integration for long-term localization accuracy in robotics mapping applications.
    </div>
    <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Ro-Bots/tree/main/icp-slam-the-ro-bots">📂 Code</a>
    <a target="_blank" class="tab_paper" href="#">📊 Results</a>
  </div>
</div>

<div class="project-card featured-card">
  <div class="project-title">
    Theo Jansen Walking Mechanism
    <span class="featured-badge">FEATURED</span>
  </div>
  <span class="project-tags">Mechatronics</span>
  <span class="project-tags">Mechanism Design</span>
  <span class="project-tags">Kinematics Simulation</span>
  <span class="project-tags">Hardware Integration</span>
  <div class="project-text">
    Designed and fabricated a <b>planar walking mechanism</b> based on the Theo Jansen linkage—a biomimetic leg design known for smooth, energy-efficient gait patterns. Developed a forward kinematic model in Python to simulate foot trajectory and optimize gait parameters before physical implementation.
    <br><br>
    Fabricated the linkage using laser-cut acrylic components and programmed Dynamixel servos for coordinated multi-leg motion control. The project integrated analytical modeling, CAD design (SolidWorks), and embedded systems programming to achieve stable, adaptive locomotion on varied terrain.
    <div class="impact-note">
      <b>Impact:</b> Successfully demonstrated bio-inspired robotics design principles with hardware validation, bridging simulation and real-world deployment.
    </div>
    <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Techamronics">📂 Code</a>
    <a target="_blank" class="tab_paper" href="https://iiithydresearch-my.sharepoint.com/:p:/g/personal/shreya_bollimuntha_research_iiit_ac_in/EQVsGRQuhVFDsP3tfNkVm9wBOm5G-yeFYun7OkPFT8wzCw?e=cdbcKs">📊 Presentation</a>
  </div>
</div>

<!-- ============================================ -->
<!-- ROBOTICS: MOTION PLANNING & PERCEPTION -->
<!-- ============================================ -->
<div class="sub_heading" id="robotics">🤖 Robotics Projects</div>

<details>
  <summary>Motion Planning & Control</summary>
  
  <div class="project-card">
    <div class="project-title">Robotics Planning & Navigation (RPN)</div>
    <span class="project-tags">Path Planning</span>
    <span class="project-tags">RRT</span>
    <span class="project-tags">MPC</span>
    <span class="project-tags">Bernstein Polynomials</span>
    <span class="project-tags">Python</span>
    <span class="project-tags">PyBullet</span>
    <div class="project-text">
      Implemented advanced planning algorithms for holonomic and non-holonomic robots in 2D PyBullet simulation environments:
      <ul>
        <li><b>RRT (Rapidly-exploring Random Tree):</b> Developed probabilistic path planning for safe navigation around dynamic and static obstacles with collision checking.</li>
        <li><b>Model Predictive Control (MPC):</b> Designed MPC using the MPPI (Model Predictive Path Integral) update rule for unicycle kinematics under velocity, acceleration, and lane-keeping constraints.</li>
        <li><b>Bernstein Polynomial Trajectories:</b> Modeled smooth, differentiable trajectories for non-holonomic robots using Bernstein basis functions, incorporating obstacle avoidance and waypoint optimization via the CEM (Cross-Entropy Method) update rule.</li>
      </ul>
      Generated simulation videos, trajectory visualizations, and quantitative performance metrics (path length, smoothness, compute time) to validate algorithm effectiveness.
      <br><br>
      <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Robotics-Planning-and-Navigation">📂 Code</a>
    </div>
  </div>
</details>

<details>
  <summary>Perception & Sensor Fusion</summary>

  <div class="project-card">
    <div class="project-title">Stereo Dense Reconstruction</div>
    <span class="project-tags">3D Vision</span>
    <span class="project-tags">Depth Estimation</span>
    <span class="project-tags">OpenCV</span>
    <span class="project-tags">Open3D</span>
    <div class="project-text">
      Developed a <b>dense 3D reconstruction pipeline</b> using OpenCV's Semi-Global Block Matching (SGBM) algorithm to compute disparity maps from stereo image pairs. Generated detailed colored point clouds with Open3D for robotic scene understanding and navigation in 3D environments.
      <br><br>
      Applied WLS (Weighted Least Squares) filtering to refine disparity maps and reduce noise, enabling accurate depth perception for autonomous manipulation and obstacle avoidance tasks.
      <br><br>
      <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Ro-Bots/tree/main/stereo-dense-reconstruction-the-ro-bots">📂 Code</a>
    </div>
  </div>

  <div class="project-card">
    <div class="project-title">Camera–IMU Calibration</div>
    <span class="project-tags">Sensor Fusion</span>
    <span class="project-tags">Extrinsic Calibration</span>
    <span class="project-tags">ROS2</span>
    <span class="project-tags">RealSense</span>
    <div class="project-text">
      Developed a <b>precise camera–IMU extrinsic calibration pipeline</b> using ROS2 and Intel RealSense D435i sensors. Estimated the 6-DOF transformation between camera and IMU frames to enable tightly-coupled sensor fusion for visual-inertial odometry (VIO).
      <br><br>
      Achieved &lt;2° orientation MSE through batch optimization of synchronized image-IMU measurements, improving motion tracking accuracy for mobile robot localization.
      <br><br>
      <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Ro-Bots/tree/main/imu-camera-callibration-the-ro-bots">📂 Code</a>
    </div>
  </div>
</details>

<!-- ============================================ -->
<!-- COMPUTER VISION -->
<!-- ============================================ -->
<div class="sub_heading" id="vision">👁️ Computer Vision Projects</div>

<div class="project-card">
  <div class="project-title">Enhancing Weak Planetary Signals in High-Contrast Exoplanet Imaging using Iterative RPCA</div>
  <span class="project-tags">Astrophysics</span>
  <span class="project-tags">Computer Vision</span>
  <span class="project-tags">Robust PCA</span>
  <span class="project-tags">Signal Processing</span>
  <span class="project-tags">Python</span>
  <div class="project-text">
    Developed a <b>novel iterative Robust Principal Component Analysis (RPCA) model</b> integrating SVD-based low-rank decomposition and Angular Differential Imaging (ADI) for separating faint planetary signals from overwhelming stellar noise in high-contrast imaging data.
    <br><br>
    Applied the method to ESO–VLT SPHERE observations of β Pictoris b, achieving <b>uniform SNR enhancement across all angular separations</b> and significantly reducing quasi-static speckle noise that typically dominates direct exoplanet detection.
    <div class="impact-note">
      <b>Impact:</b> This approach improves the detectability of faint exoplanets in archival data, enabling reanalysis of existing datasets for new discoveries without additional observing time.
    </div>
    <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Iterative-RPCA-Exoplanet-Imaging">📂 Code</a>
  </div>
</div>

<details>
  <summary>Computer Vision Course Projects — Detection, Segmentation & Multimodal Learning</summary>

  <div class="project-card">
    <div class="project-title">Computer Vision Course Projects</div>
    <span class="project-tags">Deep Learning</span>
    <span class="project-tags">PyTorch</span>
    <span class="project-tags">OpenCV</span>
    <span class="project-tags">YOLO</span>
    <span class="project-tags">U-Net</span>
    <span class="project-tags">CLIP</span>
    <div class="project-text">
      Explored classical and modern computer vision approaches across multiple problem domains:
      <ul>
        <li><b>Image Classification:</b> Implemented handwritten digit recognition on MNIST using classical methods (SIFT + Bag of Visual Words + SVM) and deep learning (CNNs, Vision Transformers). Analyzed hyperparameter effects on accuracy and data efficiency.</li>
        <li><b>Detection & Tracking:</b> Developed Viola–Jones face detector with IoU-based multi-frame tracking; fine-tuned YOLOv8 on Open Images dataset, comparing pretrained vs. scratch training and varying dataset sizes.</li>
        <li><b>Semantic Segmentation:</b> Trained U-Net models on Cityscapes dataset, investigating the impact of skip connections on mean IoU performance and convergence speed.</li>
        <li><b>Multimodal Learning:</b> Compared CLIP (Contrastive Language–Image Pretraining) and ImageNet-pretrained ResNet-50 encoders for zero-shot classification; evaluated FP16 mixed-precision inference for speedup and memory savings.</li>
      </ul>
      <b>Tools:</b> Python, PyTorch, OpenCV, scikit-learn, Ultralytics YOLO, Weights & Biases, NumPy, Matplotlib
      <br><br>
      <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Computer-Vision">📂 Code</a>
    </div>
  </div>
</details>

<details>
  <summary>Digital Image Processing — Classical Algorithms from Scratch</summary>

  <div class="project-card">
    <div class="project-title">Digital Image Processing</div>
    <span class="project-tags">Image Processing</span>
    <span class="project-tags">Filtering</span>
    <span class="project-tags">Edge Detection</span>
    <span class="project-tags">Morphology</span>
    <span class="project-tags">Python</span>
    <span class="project-tags">OpenCV</span>
    <div class="project-text">
      Implemented classical image processing algorithms <b>from scratch</b> to build foundational understanding of spatial, frequency, and feature-space techniques:
      <ul>
        <li><b>Core Operations:</b> Pixel-level brightness/contrast adjustments, grayscale ↔ pseudocolor conversion, video frame manipulation.</li>
        <li><b>Histogram Processing:</b> Custom histogram equalization; bit-depth quantization; LSB steganography for encryption/decryption.</li>
        <li><b>Filtering & Edge Detection:</b> Manual implementation of mean, median, Gaussian, bilateral, Sobel, Prewitt, Roberts, and Laplacian filters; spatial vs. frequency domain analysis.</li>
        <li><b>Morphological Processing:</b> Segmented overlapping coins; signature verification via custom erosion, dilation, and skeletonization.</li>
        <li><b>Feature Detection:</b> Otsu and adaptive thresholding; Hough line/circle detection; Harris corner detection for geometric feature extraction.</li>
      </ul>
      <b>Tools:</b> Python, NumPy, OpenCV, Matplotlib, scikit-image
      <br><br>
      <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Digital-Image-Processing">📂 Code</a>
    </div>
  </div>
</details>

<!-- ============================================ -->
<!-- MACHINE LEARNING -->
<!-- ============================================ -->
<div class="sub_heading" id="ml">🧠 Machine Learning Projects</div>

<details>
  <summary>Statistical Methods in AI (SMAI) — Course Projects</summary>

  <div class="project-card">
    <div class="project-title">Statistical Methods in Artificial Intelligence | IIIT Hyderabad</div>
    <span class="project-tags">Machine Learning</span>
    <span class="project-tags">Deep Learning</span>
    <span class="project-tags">Python</span>
    <span class="project-tags">PyTorch</span>
    <span class="project-tags">Statistical Learning Theory</span>
    <div class="project-text">
      Developed ML and deep learning pipelines from scratch and using libraries, demonstrating strong understanding of statistical learning theory, model evaluation, and neural architectures:
      <ul>
        <li>Implemented <b>Decision Trees, kNN, Naive Bayes, GMMs</b> from scratch with custom clustering metrics.</li>
        <li>Built <b>PCA-based Eigenface Recognition</b> system for face classification.</li>
        <li>Trained <b>CNNs and Autoencoders</b> on CIFAR-10 and MNIST; developed <b>RNN–LSTM</b> networks for IMDB sentiment analysis.</li>
        <li><b>Kaggle Mini-Project:</b> Age prediction from facial images using VGG16 transfer learning, achieving top leaderboard performance.</li>
      </ul>
      <b>Tools:</b> Python, NumPy, scikit-learn, PyTorch, Matplotlib, pandas
      <br><br>
      <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Statistical-Methods-in-AI">📂 Code</a>
    </div>
  </div>
</details>

<details>
  <summary>Applied AI & ML Projects</summary>

  <div class="project-card">
    <div class="project-title">Megathon – Social Media Personality Analysis</div>
    <span class="project-tags">Android</span>
    <span class="project-tags">NLP</span>
    <span class="project-tags">Psychometrics</span>
    <div class="project-text">
      Developed an Android application that analyzes social media activity and psychometric test results to classify users as better suited for <b>tech or sales roles</b>. The app outputs percentage match scores for each category, aiding recruiters in candidate shortlisting through automated personality profiling.
      <br><br>
      <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Social-Media-Personality-Analysis">📂 Code</a>
    </div>
  </div>

  <div class="project-card">
    <div class="project-title">Movie Recommender System</div>
    <span class="project-tags">Collaborative Filtering</span>
    <span class="project-tags">Matrix Factorization</span>
    <span class="project-tags">Python</span>
    <div class="project-text">
      Built a movie recommender system using <b>collaborative filtering and matrix factorization</b> (SVD-based) to provide personalized recommendations based on user rating patterns and preferences.
      <br><br>
      <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Recommender-Systems">📂 Code</a>
    </div>
  </div>

  <div class="project-card">
    <div class="project-title">Precog Research Projects — Election Analysis</div>
    <span class="project-tags">Text Classification</span>
    <span class="project-tags">NLP</span>
    <span class="project-tags">Data Analysis</span>
    <span class="project-tags">Computer Vision</span>
    <div class="project-text">
      Contributed to political data analysis projects under the Precog research group at IIIT Hyderabad:
      <ul>
        <li><b>Election Classification:</b> Implemented classification models to categorize election-related social media posts for large-scale political discourse analysis.</li>
        <li><b>Election Spends Analysis:</b> Analyzed and classified election advertisement data to estimate campaign expenditures using multimodal (text + image) analysis pipelines.</li>
      </ul>
      <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Election-Classification">📂 Code 1</a>
      <a target="_blank" class="tab_paper" href="https://github.com/harsha20032020/Election-Ads/">📂 Code 2</a>
      <a target="_blank" class="tab_paper" href="https://github.com/harsha20032020/ElectionsSpendsProject">📂 Code 3</a>
    </div>
  </div>
</details>

<!-- ============================================ -->
<!-- INTERDISCIPLINARY RESEARCH -->
<!-- ============================================ -->
<div class="sub_heading" id="interdisciplinary">🔬 Interdisciplinary Research</div>
<p class="section-description">
  Exploring cognitive neuroscience and behavioral research—skills transferable to human-robot interaction, AR/VR interfaces, and decision-making models.
</p>

<div class="project-card">
  <div class="project-title">Effects of Virtual Reality on Spatial Memory Encoding — Cognitive Neuroscience</div>
  <span class="project-tags">Cognitive Neuroscience</span>
  <span class="project-tags">Virtual Reality</span>
  <span class="project-tags">Experimental Design</span>
  <span class="project-tags">Statistical Analysis</span>
  <div class="project-text">
    Designed a <b>between-subjects controlled experiment</b> investigating how immersive VR environments vs. real-world settings affect spatial memory encoding and retrieval. Participants (ages 18–40) were trained and tested across three complexity levels: object placement, route navigation, and maze navigation.
    <br><br>
    Measured recall alignment error, response times, and hypothesized brain activation patterns (hippocampus, medial entorhinal cortex). Results demonstrated <b>superior spatial recall performance in real-world encoding</b>, highlighting sensorimotor engagement's critical role in memory consolidation and revealing VR's limitations in complex spatial tasks.
    <div class="impact-note">
      <b>Relevance to Robotics:</b> Understanding human spatial cognition informs the design of AR/VR-based robot teleoperation interfaces and human-robot collaboration in shared physical-virtual environments.
    </div>
    <a target="_blank" class="tab_paper" href="Projects/LnM/LNM Project - Effects of Virtual Reality on Spatial Memory Encoding_submission.pdf">📄 Report</a>
  </div>
</div>

<div class="project-card">
  <div class="project-title">Gender Differences in Reward-Based Effort — Behavioral Research</div>
  <span class="project-tags">Behavioral Research</span>
  <span class="project-tags">Decision Making</span>
  <span class="project-tags">Statistical Analysis</span>
  <span class="project-tags">Mixed-Effects Models</span>
  <div class="project-text">
    <b>Replicated and extended a <i>Nature</i> study</b> on gender differences in cost-benefit decision-making by analyzing effort allocation across 81 participants. Applied advanced statistical methods including mixed-effects models, Kruskal-Wallis tests, and post-hoc pairwise comparisons.
    <br><br>
    Confirmed that <b>vagus nerve stimulation (VNS) significantly enhances reward-driven motivation (p &lt; 0.001)</b> and demonstrated that gender independently modulates effort maintenance (Cohen's d = 0.338). Provided new insights into the interplay between physiological interventions and behavioral decision-making processes.
    <div class="impact-note">
      <b>Relevance to Robotics:</b> Understanding effort allocation and motivation models can inform reward function design in reinforcement learning for autonomous systems and human-robot collaboration frameworks.
    </div>
    <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Gender-Reward-Effort-Behavioral-Study/blob/main/Project_Analysis.ipynb">📂 Code</a>
    <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Gender-Reward-Effort-Behavioral-Study/blob/main/BRSM_Project_Final_Report.pdf">📄 Report</a>
  </div>
</div>