<!DOCTYPE html>
<!-- saved from url=(0065)http://twitter.github.io/bootstrap/examples/starter-template.html -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <title>Bootstrap, from Twitter</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- Le styles -->
    <link href="http://twitter.github.io/bootstrap/assets/css/bootstrap.css" rel="stylesheet">
    <style>
      body {
        padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
      }
    </style>
    <link href="http://twitter.github.io/bootstrap/assets/css/bootstrap-responsive.css" rel="stylesheet">

    <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="../assets/js/html5shiv.js"></script>
    <![endif]-->

    <!-- Fav and touch icons -->
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="http://twitter.github.io/bootstrap/assets/ico/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="http://twitter.github.io/bootstrap/assets/ico/apple-touch-icon-114-precomposed.png">
      <link rel="apple-touch-icon-precomposed" sizes="72x72" href="http://twitter.github.io/bootstrap/assets/ico/apple-touch-icon-72-precomposed.png">
                    <link rel="apple-touch-icon-precomposed" href="http://twitter.github.io/bootstrap/assets/ico/apple-touch-icon-57-precomposed.png">
                                   <link rel="shortcut icon" href="http://twitter.github.io/bootstrap/assets/ico/favicon.png">
  </head>

  <body style="">

    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="brand" href="http://twitter.github.io/bootstrap/examples/starter-template.html#">Project name</a>
          <div class="nav-collapse collapse">
            <ul class="nav">
              <li class="active"><a href="http://twitter.github.io/bootstrap/examples/starter-template.html#">Home</a></li>
              <li><a href="http://twitter.github.io/bootstrap/examples/starter-template.html#about">About</a></li>
              <li><a href="http://twitter.github.io/bootstrap/examples/starter-template.html#contact">Contact</a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>

    <div class="container">

	<center>
      <h1>Search engine</h1>
	  <form action="/search"  method="post">
		  <input type="text" class="input-large search-query" name="query"/>
		  <button class="btn btn-primary" id="search-button" type="submit"><i class="icon-search icon-white"></i> Search</button>
	  </form>

	</center>
	<ul class="breadcrumb">
	  <li>{{q}}: {{len(r)}} results</li>
	</ul>
	<table class="table table-hover" id="test3">
	%for i in range(0, len(r)):
	<tbody>
	    <tr id="test.html"><td id="test2.html">{{" ".join(r[i]['text'][:100])}}</td></tr>
	  
	%end
	</tbody>
	  </table>
    </div> <!-- /container -->

    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <!--
    <script src="./test_files/jquery.js"></script>
    <script src="./test_files/bootstrap-transition.js"></script>
    <script src="./test_files/bootstrap-alert.js"></script>
    <script src="./test_files/bootstrap-modal.js"></script>
    <script src="./test_files/bootstrap-dropdown.js"></script>
    <script src="./test_files/bootstrap-scrollspy.js"></script>
    <script src="./test_files/bootstrap-tab.js"></script>
    <script src="./test_files/bootstrap-tooltip.js"></script>
    <script src="./test_files/bootstrap-popover.js"></script>
    <script src="./test_files/bootstrap-button.js"></script>
    <script src="./test_files/bootstrap-collapse.js"></script>
    <script src="./test_files/bootstrap-carousel.js"></script>
    <script src="./test_files/bootstrap-typeahead.js"></script>-->
    <script type="text/javascript" src="http://code.jquery.com/jquery-1.9.1.js"></script>
    <script type="text/javascript" src="static/script.js" charset="utf-8"></script>
  

</body></html>
