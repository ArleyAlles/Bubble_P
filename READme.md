<div style="text-align: center; font-size: 40px; font-weight: bold;">
P-bubble
</div>

*Author*: **Arley A. Cruz**
### The structure of code is divided into:
	
1. **main.py**
2. **Points.py**
3. **Bubble.py**
4. **Parameters.py**
5. **Eos.py**
6. **Experimental_output.py**
7. **requirements.txt**

### Explanation of each *.py* file:
1. The file ***main.py*** is the user-executable part of the program.


2. The file ***Points.py*** contains the experimental points of
saturation process. These data are:
    - **x**: Molar fraction in the liquid phase;
   
    OBS: To insert a new experimental condition, the user must add the experimental
points here, as the same way as the points already added.


3. The file ***Bubble.py*** is the main part of the code which contains the 
saturation point calculation by *VER REFERENCIA*. In this case ϕ-ϕ approach was adopted and 
Peng-Robinson EoS was used for calculating the deviation from ideality. 

4. The file ***Parameters.py*** gathers all input parameters necessary for running
the code. Such parameters are:
        
    - *R*: Universal gas constant [float];
    - *Tc*: Critical temperature [array - float];
    - *Pc*: Critical pressure [array - float];
    - *w*: Acentric factor[array - float];
    - *Kij*: Binary interaction parameter [array - float];
    - *a*: Antoine parameters of each components [array - float];
    - *Psat*: Saturation pressure by Antoine equation [array - float].

   OBS: To insert a new condition, the user must add the parameters here, 
as the same way as the points already added.


5. The file ***EoS.py*** contains the equation of state used for calculating the fugacity coefficient (ϕ) 
in the both phases
6. The file ***Experimental_output*** contains experimental points (P and y) for comparison 
with calculated results. Such comparison if accomplished in the method AARD in the ***Bubble.py***.


6. **requirements.txt** is the list of all python extensions needed for running the code.To install such extensions use the command:
    
         pip install -r requirements.txt 