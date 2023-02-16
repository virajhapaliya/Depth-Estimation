# Depth-Estimation

For the depth estimation I have used the Intel's Hybrid and Large models. Check the output give below.

# How to run

> pip install -r requiremens.txt

- for hybrid model

```
python depth_estimation.py -input Input\test3.jpg -save True -model large
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
