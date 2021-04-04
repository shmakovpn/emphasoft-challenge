# EmphaSoft challenge

## The story

In US, taxes are often complex and require many different PDF forms and posted informational
notices. IRS service keeps records of the current tax year's forms and historical forms going back
many years online on [irs.gov](https://irs.gov).

## Challenge

For this challenge you must write two different utilities for searching IRS tax forms:

- Taking a list of tax form names (ex: "Form W-2", "Form 1095-C"), search the website and
return some informational results. Specifically, you must return the "Product Number", the
"Title", and the maximum and minimum years the form is available for download. The
results should be returned as json, in the format of the following example:

 ```json
 [
   {
     "form_number": "Form W-2",
     "form_title": "Wage and Tax Statement (Info Copy Only)",
     "min_year": 1954,
     "max_year": 2021
   }
   ...
 ]
 ```




