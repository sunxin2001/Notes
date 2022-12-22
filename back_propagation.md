#This is my first time to write a note on github!

for days i learned deep learning, i only had a fuzzy concept about back propagation, how it flows from output to parameters  

so i am about to review the details of propagation to solid my knowledge!  

![image](https://user-images.githubusercontent.com/111692657/209224715-e6e25448-b78b-43d2-b254-46810484e2d3.png)

a really simple neural networking containing an input layer, a hidden layer, and an output layer.  

in neural networking the first thing we have to do is to minimize the loss function, taking MSE as an example.

![image](https://user-images.githubusercontent.com/111692657/209225464-472deeab-e30d-4d31-b98f-1d1faa2e495b.png)

at the beginning of forward propagation, we have initialized the parameters and we have to update these parameters to reach minimial loss.

![image](https://user-images.githubusercontent.com/111692657/209225993-bcd44a23-4d30-4015-90dd-d1c7edd855c8.png)

we have to see effects of parameters and their weights on outputs.  

![image](https://user-images.githubusercontent.com/111692657/209226594-409ec980-0c2d-4944-b218-59f4e4283327.png)

here we use a sigmoid function as activation function.

