Exercise 1: Probabilistic Graphical Model

My Approach:

My first solution was to use the existing Pomegranate Python library. I
successfully created the model and was able to use it to create predictions
both with and without input values. The code for the model create can be found
in Pomegranate.py.

Secondly I decided to simulation the process from scratch to see if the values
given by the Pomegranate match the simulation. They do indeed match and the
code for this brute force simulation is found in Simulation.py.

After these two approaches I decided I should learn more about the underlying
algorithms in the Pomegranate library. I learnt the variable elimination
algorithm from this PDF document
https://cedar.buffalo.edu/~srihari/CSE674/Chap9/9.3-VE-Algorithm.pdf that I
found online. I was able to successfully implement this algorithm. My
factor classes required for my implementation of the algorithm are in
Factor_Class.py and the creation of the specific network in this problem is in
Variable_Elimination.py. This method also successfully predicts the
probabilites without any given input values. I have not implemented this
algorithm from scratch for given input values but believe I could do so without
too much difficulty given more time. 

Running Main.py will output predictions for all 3 approaches I took. For the
first 2 it will also show the probabilities with some given inputs.

Running Variable_Elimination_Surface.py will run my VE algorithm built from
scratch to produce this surface graph which I included as the description said
to plot away. 

<img src= "https://github.com/PJF98/BayesianNetwork/blob/main/Probs_Plot.png" title="Surface Plot" />

Points For Discussion:

In order to dynamically quantify the best information to make a more accurate
prediction we could look at the difference in probabilites between when we
predict given true and false values. A large difference would indicate this
information is crucial to our predictions.

In order to validate an expert constructed network model we'd have to have a
large dataset with real world examples of the data. Then we could see the
difference in probabilities of our model and the real world probabilites. 

The complexity added with a Gaussian Distribution for example is that when
combining factors we have to multiply distributions and then instead of summing
to remove the variable we have to integrate over a variable. It is unlikely
these distributions are integratable and hence we would have to numerically
approximate the solution adding a lot of complexity to the algorithm.

A key problem of use sampling techniques is that events that happen with
low probability will be less accurately predicted as they will occur in fewer
of the samples giving a greater error. 

The difficulty of using exact inference is that it's time consuming (eg. very
difficult to optimise the order of nodes in variable elimination for example) and not
possible in a lot of cases. The sampling techniques give us a faster but less
accurate alternative. 

Networks of 1000s of nodes will be very time consuming and difficult to
optimise. They may also be very sensitive to small changes in individual nodes. 

The challenges when handling many requests simultaneously in a production
evnironment is efficiently working out several probabilities quickly without
having to solve the network completely each time. 

NP-hard is a familiar concept to me. I am aware that exact inference is an
NP-hard problem meaning that it's highly unlikely that a polynomial time
algorithm exists and hence it's extremely costly to do efficiently. In addition
I have read optimially chosing the order of nodes for variable elimination is
also NP.

I have just started reading about d-seperation at this link
http://bayes.cs.ucla.edu/BOOK-2K/d-sep.html. My understanding isn't perfect but
I have a reasonable understanding of the idea. I expect this ties into not
having to solve the whole network so simultaneous requests in production can be
solved more efficiently. 
