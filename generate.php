<?php


$consumerKey = $argv[0];
$consumerSecret = $argv[1];
$oAuthToken = $argv[2];
$oAuthSecret = $argv[3];

require_once('twitteroauth.php');

$handle = fopen("quotes.txt", "r") or die("Couldn't get handle");
  if ($handle) {
    while (!feof($handle)) {
        $buffer = fgets($handle, 4096);
        // Process buffer here..

       $tweet = new TwitterOAuth($consumerKey, $consumerSecret, $oAuthToken, $oAuthSecret);
       $message = "$buffer";
       $tweet->post('statuses/update', array('status' => "$message"));
       sleep(36);

    }
    fclose($handle);
  }


?>
