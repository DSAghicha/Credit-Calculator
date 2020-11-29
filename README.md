<p align="RIGHT"> <a href ="https://github.com/DSAghicha/Credit-Calculator/blob/main/FR_README.md">FR</a></p>

# Credit Calculator

#### Created using [Python 3.8](https://www.python.org/)

This program is useful to calculate Annuity Payments and Differentiated Payments.

Quick Navigation:
- [Installation](README.md#installation)
- [Programme Details](README.md#programme-details)
- [Annuity Payment](README.md#annuity-payment)
- [Differentiated Payment](README.md#differentiated-payment)
- [Credits](README.md#credits)

### Installation

   Install Python from [here](https://www.python.org/downloads/)
   
   To check if Python is installed properly open Command Prompt on your PC and type the following code:
   ```python  --version``` 
   
   This should return Python version number if it is correctly installed

### Programme Details

Sometimes we need some extra money so, we decide to take a loan.

This loan can be repaid either **monthly annuity** or **differentiated payments**.

This programme can be used in two formats:

1. Command Line Interface
   
   **Steps**

   - Download **cli.zip** from [Releases](https://github.com/DSAghicha/Credit-Calculator/releases/latest) and unzip it on your PC.
    
     This zip file will have one directory which will have two files ```main.py``` & ```cli.py```.
   - Open Terminal in this directory and run ```python cli.py```.
   
     Alternatively, you can open it in your favourite code editor and run it from there as well.
        
2. Command Line Arguments
   
   **Steps**
   
   - Download **cl_args.zip** from [Releases](https://github.com/DSAghicha/Credit-Calculator/releases/latest) and unzip it on your PC.
   
     This zip file will have one directory which will have two files ```main.py``` & ```arg_based.py```.
   - Open Terminal in this directory and run ```python arg_based.py --help```.
   
      You will see the list of all optional arguments which you need to follow.The script will detect the one that is not provided and calculate it's result.
      
      ```python arg_based.py --all optional arguments```

__*For Demo: [Check out this video]()*__

### Annuity Payment

*Annuity payment* remains unchanged throughout the duration of the credit agreement. This means that each month you will pay for the loan by equal installments, which consist of accrued interest per loan and part in principal.

The formula to calculate *Annuity payment* is as follows:

![annuity_formula](https://user-images.githubusercontent.com/53931676/100551371-fff26380-32a5-11eb-88cb-72255d4241b4.png)

The formulae to calculate Loan Principal and number of payments are as follows:

![loan_principal](https://user-images.githubusercontent.com/53931676/100551391-20222280-32a6-11eb-88bc-0e885ad567e8.png)

![period](https://user-images.githubusercontent.com/53931676/100551405-3af49700-32a6-11eb-8f81-2f48f8eeb2e3.png)

<p>
    where,<br>
    <b>A<sub>ordinary_annuity</sub></b> = annuity payment;<br>
    <b>P</b> = loan principal;<br>
    <b>i</b> = nominal (monthly) interest rate. Usually, it’s 1/12 of the annual interest rate, and usually, it’s a floating value, not a percentage;<br>
    <b>n</b> = number of payments. This is usually the number of months in which repayments will be made.
</p>

### Differentiated Payment

In the case of *differentiated payments*, your monthly payment will decrease because the debt will be extinguished in equal installments and  interest will accrue monthly on the balance of the debt.

The formula to calculate *Differentiated Payment* is as follows:

![diff_formula](https://user-images.githubusercontent.com/53931676/100551415-58296580-32a6-11eb-859c-2d35ad7d704e.png)

<p>
    where,<br>
    <b>D<sub>m</sub></b> = mth differentiated payment;<br>
    <b>P</b> = loan principal;<br>
    <b>i</b> = nominal (monthly) interest rate. Usually, it’s 1/12 of the annual interest rate, and usually, it’s a floating value, not a percentage;<br>
    <b>n</b> = number of payments. This is usually the number of months in which repayments will be made;<br>
    <b>m</b> = current repayment month.
</p>

### Credits

This project was a part of Hyperskill's teaching program to teach Python.

```arg_based.py``` & ```main.py``` files in  particular were submitted as my coursework.

**[Hyperskill](https://hyperskill.org/)** is a platform created by Jet Brains Academy which offers interactive project-based learning combined with powerful, professional development tools.

Be sure to check them out...

Let me know if you have any other queries...
