<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>\\
%default = "Nutritional Info of Common Raw Fruits and Veggies"
{{title if defined('title') else default}}</title>
<style type="text/css">
body {
    margin: 25px;
    padding: 25px;
}
section {
    border: 1px dotted #555;
}
section p {
    padding: 25px;
}
section p.bigmessage {
    font-size: 3em;
    text-align: center;
    font-weight: bold;
}
section h1 {
    text-align: center;
}
a, a:visited {
    color: #663;
    text-decoration: none;
}
th, td {
    text-align: left;
    padding: 10px;
}
label {
    display: block;
    margin: 15px;
}
form.buttons {
    text-align: center;
}
footer {
    margin-top: 25px;
    text-align: center;
}
</style>
</head>
<body>

<section>
%include
</section>

<footer>
<a href="http://validator.w3.org/check/referer">
<strong> HTML </strong> Valid! </a> |
<a href="http://jigsaw.w3.org/css-validator/check/referer?profile=css3">
<strong> CSS </strong> Valid! </a>
</footer>

</body>
</html>
