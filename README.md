# Depth-Estimation

For the depth estimation I have used the Intel's Hybrid and Large models. Check the output give below.

# How to run

```
pip install -r requiremens.txt
```

- For Hybrid Model

```
python depth_estimation.py -input Input\test3.jpg -save True
```

- For Large Model

```
python depth_estimation.py -input Input\test3.jpg -save True -model large
```

- Params

```
-input : Single image path
-save :  To save the images in folder
-output : To save the images in given folder
-show_image :  Will show the generate output image directly
-model : Depth model type
```

# Output Samples

## "Hybrid" Model Ouptut

<p float="left">
  <img src="Input\test1.jpg" width="280" />
  <img src="output\test1_hybrid_depth.jpg" width="280" /> 
</p>
<p float="right">
  <img src="Input\test2.jpg" width="280" />
  <img src="output\test2_hybrid_depth.jpg" width="280" /> 
</p>
<p float="left">
  <img src="Input\test3.jpg" width="280" />
  <img src="output\test3_hybrid_depth.jpg" width="280" /> 
</p>

## "Large" Model Ouptut

<p float="left">
  <img src="Input\test1.jpg" width="280" />
  <img src="output\test1_large_depth.jpg" width="280" /> 
</p>
<p float="right">
  <img src="Input\test2.jpg" width="280" />
  <img src="output\test2_large_depth.jpg" width="280" /> 
</p>
<p float="left">
  <img src="Input\test3.jpg" width="280" />
  <img src="output\test3_large_depth.jpg" width="280" /> 
</p>
