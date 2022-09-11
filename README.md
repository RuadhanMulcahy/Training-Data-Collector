# Training Data Collector
Selenium web scraping application for collecting labelled training data from chess.com.

## Requirements
- Python (Current version tested with 3.9.7).
- Selenium Chromium web driver.

## Run
To run the application use run.py followed by arguments shown below:
- "--username" Username of chess profile to scrape data from. (Required)
- "--game_id" Game ID of game to scrape data from - If not set all users games will be scraped.
- "--highlight" Will highlight elements in image for demo purposes.
- "--style" Sets board style - default is 1.

## Sample OutputTraining-Data-Collector

### Training Image
Board has been extracted from the original screenshot and has been resized, re-positioned <br/>and super imposed on a random background image <br/> <br/>
<img src="https://github.com/RuadhanMulcahy/Training-Data-Collector/blob/main/sample_output/48340232755_move_169_1.png" width="60%">

### Corresponding Label File
Label file in darknet format with location of each element from the above image:

  13 0.512109375 0.6854166666666667 0.33046875 0.5875 <br/>
  12 0.450390625 0.6493055555555556 0.04140625 0.07361111111111111 <br/>
  12 0.656640625 0.6493055555555556 0.04140625 0.07361111111111111 <br/>
  2 0.491796875 0.9423611111111111 0.04140625 0.07361111111111111 <br/>
  4 0.491796875 0.7229166666666667 0.04140625 0.07361111111111111 <br/>
  4 0.656640625 0.6493055555555556 0.04140625 0.07361111111111111 <br/>
  9 0.408984375 0.4284722222222222 0.04140625 0.07361111111111111 <br/>
  3 0.574609375 0.5756944444444444 0.04140625 0.07361111111111111 <br/>

