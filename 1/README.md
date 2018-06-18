# Task

Task is to write a BOT, which can extract odds/probability for all the teams in World Cup 2018 Win Outright market from links given below and generate a real-time matrix from it. 
Code should either print matrix to screen or save it in file, which should update at given interval (by default every 5 minutes). 

Preferably:
 - use text processing/analysis to navigate to correct match link from home URL instead of hardcoding the start URL.
 - team names can also be used as parameter(expected given) to locate correct odds elements on page.

For example the matrix should have following format.

<table>
	<tr>
		<th>Team</th>
		<th>Site1</th>
		<th>Site2</th>
		<th>Site3</th>
		<th>Site4</th>
	</tr>
	<tr>
		<td>Team1</td>
		<td> </td>
		<td> </td>
		<td> </td>
		<td> </td>
	</tr>
	<tr>
		<td>Team2</td>
		<td> </td>
		<td> </td>
		<td> </td>
		<td> </td>
	</tr>
	<tr>
		<td>Team3</td>
		<td> </td>
		<td> </td>
		<td> </td>
		<td> </td>
	</tr>
	<tr>
		<td>Team4</td>
		<td> </td>
		<td> </td>
		<td> </td>
		<td> </td>
	</tr>
	<tr>
		<td>Team5</td>
		<td> </td>
		<td> </td>
		<td> </td>
		<td> </td>
	</tr>
	<tr>
		<td>Team6</td>
		<td> </td>
		<td> </td>
		<td> </td>
		<td> </td>
	</tr>
</table>

Points will be given based on:
1. Code correctness 
2. Code design and architecture (Preferably don’t use any frameworks, like Scrapy etc)
3. Speed of execution


Version 0.1
