

# Demo application: Vacalc #

The application that is developed in this demo is called _Vacalc_ and
it is a tool for calculating vacations according to the Finnish
vacation laws. Every company in Finland is required to collect and
store such vacation information and Vacalc is indented to be a simple
tool for small companies. Or it could be, if it was not just a demo.

# Business requirements #

The business requirements related to calculating vacations are got
directly from the [Annual Holidays Act](http://wiki.atdd-with-robot-framework.googlecode.com/hg/AnnualHolidaysAct.pdf). In
addition to these requirements the application must allow adding
employer information and storing it persistently.

# Development #

The application is developed in Agile and iterative manner using very
short sprints.

## Sprint 1 ##

The main requirement implemented in the first sprint was adding new
employers to the application. The detailed requirements related to
this functionality can be seen in the following examples:

  * [add\_employee.txt](http://atdd-with-robot-framework.googlecode.com/hg/atest/vacalc/add_employee.txt): The basic workflow to add employers.
  * [name\_validation.txt](http://atdd-with-robot-framework.googlecode.com/hg/atest/vacalc/name_validation.txt): Validating the provided employer name.
  * [date\_validation.txt](http://atdd-with-robot-framework.googlecode.com/hg/atest/vacalc/date_validation.txt): Validating the employment start date.

Resulting [report](http://wiki.atdd-with-robot-framework.googlecode.com/hg/results/sprint-1-end-report.html) and [log](http://wiki.atdd-with-robot-framework.googlecode.com/hg/results/sprint-1-end-log.html) files are also online.

## Sprint 2 ##

The second sprint added the functionality to calculate and show
vacations for each employer.

  * [calculate\_vacation.txt](http://atdd-with-robot-framework.googlecode.com/hg/atest/vacalc/calculate_vacation.txt): Basic workflow to see vacations.
  * [calculation\_rules.txt](http://atdd-with-robot-framework.googlecode.com/hg/atest/vacalc/calculation_rules.txt): Verifying that vacations are calculated correctly according to the law.

Results during the different phases of the sprint are available as follows:

  * Beginning, when all tests are failing: [report](http://wiki.atdd-with-robot-framework.googlecode.com/hg/results/sprint-2-start-report.html) and [log](http://wiki.atdd-with-robot-framework.googlecode.com/hg/results/sprint-2-start-log.html)
  * Middle, when some of the tests are passing: [report](http://wiki.atdd-with-robot-framework.googlecode.com/hg/results/sprint-2-middle-report.html) and [log](http://wiki.atdd-with-robot-framework.googlecode.com/hg/results/sprint-2-middle-log.html)
  * End, when all the tests pass: [report](http://wiki.atdd-with-robot-framework.googlecode.com/hg/results/sprint-2-end-report.html) and [log](http://wiki.atdd-with-robot-framework.googlecode.com/hg/results/sprint-2-end-log.html)