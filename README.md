# FSDS-PracticalAssignment2

This application uses a Logistic Regression Model based on the "Affairs Dataset" from statsmodels python library 
It determines if a woman had an affair or not based on the user input data and processing it through the trainede Logistic regression model

### Dataset Description
This dataset is derived from :
		
	Fair, Ray. 1978. “A Theory of Extramarital Affairs,” Journal of Political Economy, February, 45-61.

The data is available at http://fairmodel.econ.yale.edu/rayfair/pdf/2011b.htm

- Number of observations: 6366
- Number of variables: 9

Variable name definitions:

	rate_marriage   : How rate marriage, 1 = very poor, 2 = poor, 3 = fair,
                    4 = good, 5 = very good
	age             : Age
	yrs_married     : No. years married. Interval approximations. See
                    original paper for detailed explanation.
	children        : No. children
	religious       : How relgious, 1 = not, 2 = mildly, 3 = fairly,
                    4 = strongly
	educ            : Level of education, 9 = grade school, 12 = high
                    school, 14 = some college, 16 = college graduate,
                    17 = some graduate school, 20 = advanced degree
	occupation      : 1 = student, 2 = farming, agriculture; semi-skilled,
                    or unskilled worker; 3 = white-colloar; 4 = teacher
                    counselor social worker, nurse; artist, writers;
                    technician, skilled worker, 5 = managerial,
                    administrative, business, 6 = professional with
                    advanced degree
	occupation_husb : Husband's occupation. Same as occupation.
	affairs         : measure of time spent in extramarital affairs
    
To treat this as a classification problem, any observation of the **affairs** variable greater than zero is treated as having an affair.
