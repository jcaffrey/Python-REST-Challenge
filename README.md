
# Instructions
Fork this repository and submit a url to the forked repository with your solution.
Please provide documentation in this README explaining the following:
- How to run including any configuration needed
  - Install pipenv with `pip install pipenv`
  - Install necessary dependencies into separate envrionment by running `pipenv install`
  - Enter the virtualenv with `pipenv shell`
  - Run project with `pipenv run python server.py <port> <fileToReadFrom>`
- Any thoughts on how to expand this application in the future
  - Maybe we would want to create and store the concept of relationships between people, either familial or academic (maybe some people had the same 3rd grade teacher for example). If we had information for each students' 3rd grade teacher we could store teachers and students in separate tables and have a 1-to-Many relationship between stduents and 3rd grade teachers by adding a foreign key to what would be the students table.  Or if we wanted to represent a person's entire teacher history we could have a Many-to-Many relationship between students and teachers and join on a third table that would correlate student IDs to teacher IDs.
- What you have covered or not covered.
  - I assume good input and generally don't validate much.
  - I would have liked to play around with some of the Flask patterns that are recommended for large applications but I figured I would save that for another day. For example it would have been nice to have data models that could help validate the input and coerce the types of the inputs. It would definitley be nice to handle the logic for inferring the age of a person from their 3rd grade graduation date in the model rather than when reading the data in.
  - I thought about doing different pre-processing of the data since we knew exactly what queries we would be doing but I did not want to duplicate the data in this context and I figured it would be better to show the manipulation of the data in the methods rather than sort of blackboxing that away.
## General instructions and tasks
Read and pull in data from people.csv.
Fill in the requests in server.py where TODOs are stated in the comments.
Get as many done as you can.
If you have time create unit tests.
Feel free to add other systems to the application.
Also feel free to submit issues on this public branch with questions if you have any.

