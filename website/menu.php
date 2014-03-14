
<head>
	<link rel="stylesheet" type="text/css" href="style.css">
	<title> RIT Specials Menu </title>
</head>

<body>
	<div id = "page-wrapper">
	<h1>RIT Specials Menu</h1>
	<form method="post" action="menu.php" name="form">
	<select id="location" name="location" onchange="form.submit()">
		<option value="0">--Select Location--</option>
		<option value="Brick City">Brick City</option>
		<option value="Commons">Commons</option>
		<option value="Crossroads">Crossroads</option>
		<option value="Global Village Grille">Global Village</option>
		<option value="Gracies">Gracies</option>
		<option value="Ritz">Ritz</option>
	</select>
	</form>
<?php
	echo "<h2>" . $_POST['location'] . "</h2>";
	$con= mysqli_connect("host","user","password","database");
	//check connection
	if (mysqli_connect_errno())
		{
		echo "Failed to connect to MySQL: " . mysqli_connect_error();
		}
	
	if($_POST['location'] && $_POST['location'] != "0") {
		$location = $_POST['location'];
		$currLocation = mysqli_fetch_array(mysqli_query($con, "SELECT id FROM location where name = '" . $_POST['location'] . "';"));
		$currCategoryObject = (mysqli_query($con, "SELECT * FROM category;"));
		while($row = mysqli_fetch_array($currCategoryObject)) {
			$currCategoryArray[] = $row; 
		}
		$currFoodItemObject = (mysqli_query($con, "SELECT * FROM food_items where fk_locid = '" . $currLocation[0] . "';"));
		while($row = mysqli_fetch_array($currFoodItemObject)) {
			//All of the food items for the selected location
			$currFoodItemArray[] = $row;

		}
		//All the current food item's category Ids will go in this array
		$currFoodItemCatIdArray = array();
		foreach($currFoodItemArray as $FoodItem) {
			$currFoodItemCatId = $FoodItem[2];
			array_push($currFoodItemCatIdArray, $currFoodItemCatId);
		}
		$lastId = -1;
		
		$categories = array();
		foreach($currFoodItemCatIdArray as $curr) {
			if($curr != $lastId) {
				$lastId = $curr;
				foreach($currCategoryArray as $cat) {
					//echo "<br>";
					//echo "<br>"
					if ($cat[0] == $curr) {
						array_push($categories, $cat);
					}
				}
			}
		}			
		foreach($categories as $cat) {
			echo '<div class="location-menu-category">'; 
			echo $cat[1];
			echo "</div>\n";
			foreach($currFoodItemArray as $currFood) {
				if($cat[0] == $currFood[2]) {
					echo '<div class="location-menu-item">';
					echo $currFood[0];
					echo "</div>\n";
				}
			}
		}

	}
	mysqli_close($con);
?>

	</div> 
</body>
