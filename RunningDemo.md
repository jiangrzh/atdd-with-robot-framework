

# Preconditions #

To experiment with this demo locally, you need to first install [Mercurial](http://mercurial.selenic.com/) version control tool. Once Mercurial is installed, you can get the demo by running following command from the command line:
```
hg clone https://code.google.com/p/atdd-with-robot-framework/
```

This creates a directory named `atdd-with-robot-framework` and fetches the repository content there.

# Repository structure #

The repository contains following files and directories:

  * `atest` contains the acceptance tests and supporting code
    * `atest/vacalc` contains the Robot Framework tests
    * `atest/libraries` contains test libraries used by the tests
  * `bin` contains binary dependencies of the application
  * `src` contains application source code
  * `utest` contains some unit tests for the application
  * `start_vacalc.bat` is a script for starting the application in Windows
  * `start_vacalc.sh` is a script for starting the application in Linux/OSX

The repository content can also be browsed [online](https://code.google.com/p/atdd-with-robot-framework/source/browse/).

# Running the acceptance tests #

Acceptance test can be run using command `atest\run.bat` (in Windows) or `atest/run.sh` (in unixy machines). By default, all the tests are executed, but the script accepts all Robot Framework [command line options](http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html?r=2.6.3#all-command-line-options), for example the following command runs only the named test case:
```
atest\run.bat --test ShowVacationForEmployee
```

# Navigating the history #

When the repository is cloned using the instructions above, you will end up with the most recent revision of the demo. However, it is possible to travel back in time to some earlier stage and run the tests there. Updating the repository is done using command:
```
hg up <tagname>
```

Following tags are defined in the revision history:

  * sprint-1-end: In this revision, it is possible to add new employees to the system and view their basic information
  * sprint-2-start: The acceptance tests for calculating vacation days correctly and showing the vacation days for current year in the UI are added, but they are failing since the implementation is not yet available.
  * sprint-2-middle: Part of the newly added tests are already passing.
  * sprint-2-end: The implementation for calculating and showing vacation days is added, and all the tests are again passing.

You can also run just command `hg up` to return to the latest revision.

# Example #

```
C:\> hg clone https://code.google.com/p/atdd-with-robot-framework/
C:\> cd atdd-with-robot-framework
C:\atdd-with-robot-framework> hg up sprint-1-end
C:\atdd-with-robot-framework> atest\run.bat
C:\atdd-with-robot-framework> hg up sprint-2-start
C:\atdd-with-robot-framework> atest\run.bat
C:\atdd-with-robot-framework> hg up
C:\atdd-with-robot-framework> atest\run.bat
```