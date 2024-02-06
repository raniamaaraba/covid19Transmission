# Activity Python 11: Task 1
# File: ACT_Python_HeaderTemplate_Team355_maarabrn.py 
# Date:    12 11 2023
# By:      Rania Maaraba
# Section: 21
# Team:    355
# 
# ELECTRONIC SIGNATURE
# Rania Maaraba
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# The program calculates COVID-19 transmission rates,
# incubation rate, ,prta;otu rate, and birth coeffcient in days
# based on the user given data and a provided flow diagram.

# Enter the values for simga, mu, gamma, delta, beta 1 and 2, alpha
σ1= float(input('Enter the coefficient σ = '))
μ1= float(input('Enter the coefficient μ = '))
γ1= float(input('Enter the coefficient γ = '))
δ1 = float(input('Enter the coefficient δ ='))
β1= float(input('Enter the coefficient β1 = '))
β2= float(input('Enter the coefficient β2 = '))
α1= float(input('Enter the coefficient α = '))

#Calculates the value of F
F1 = δ1*((β1*σ1)+(γ1+μ1)*β2)
F = F1/((σ1+μ1)*(γ1+μ1)*μ1)

#calculate R
R = (1-α1)*F

print(R)

#calculate alpha sub c
α_c= 1 - (1/F)

#determine the state of society
if R == 1:
    if α1 < α_c:
        SOH = 'Endemic Statem increase public measures'
    elif α1 > α_c:
        SOH = 'No change in public health measures'        
elif R > 1: 
    if α1 < α_c: 
        SOH = 'Disease expansion state, increase Public Health Measures'
    elif α1 > α_c:
        SOH = 'No change in public health measures'
elif α1 > α_c:
    SOH = 'Disease controlled, Decreased Public Health Measures'
else:
    SOH = 'No change in public health measures'
    
print(SOH)



