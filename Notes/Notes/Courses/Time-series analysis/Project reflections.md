* Kalman filter parameters spiking when adapting
The spikes may be due to for example -0.2z-1+0.2z-2, which leads to spikes at certain values. In reality, the pole-zero plots may be moving smoothly.
* Dual-input BJ-model
Form the residuals of a single input model, and treat the residuals as a new output to model using the second input.
To choose which input for "single input", correlation matrix is a good metric to use as a "main" input to use to inverse filter
* Use FFT to find season