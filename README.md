# Training Data Collector
Selenium web scraping application for collecting labelled training data from chess.com.

## Requirements
- Python (Current version tested with 3.9.7).
- Selenium Chromium web driver.

## Sample Output
### Training Image
Board has been extracted from the original screenshot and has been resized, re-positioned and super imposed on a <br/>random background image <br/>
<img src="https://github.com/RuadhanMulcahy/Training-Data-Collector/blob/main/sample_output/48340232755_move_169_1.png" width="80%">

### Corresponding Label File
Label file in darknet format with location of each element from the above image

13 0.512109375 0.6854166666666667 0.33046875 0.5875 <br/>
12 0.450390625 0.6493055555555556 0.04140625 0.07361111111111111 <br/>
12 0.656640625 0.6493055555555556 0.04140625 0.07361111111111111 <br/>
2 0.491796875 0.9423611111111111 0.04140625 0.07361111111111111 <br/>
4 0.491796875 0.7229166666666667 0.04140625 0.07361111111111111 <br/>
4 0.656640625 0.6493055555555556 0.04140625 0.07361111111111111 <br/>
9 0.408984375 0.4284722222222222 0.04140625 0.07361111111111111 <br/>
3 0.574609375 0.5756944444444444 0.04140625 0.07361111111111111 <br/>

