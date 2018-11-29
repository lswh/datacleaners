const puppeteer = require('puppeteer');
(async() => {
  const browser = await puppeteer.launch({args: ['--no-sandbox', '--disable-setuid-sandbox']});
  const page = await browser.newPage();
  await page.setExtraHTTPHeaders({Referer: 'https://facebook.com/'}) 
  await page.goto('https://www.cnn.com/', {waitUntil: 'networkidle2'});
  var HTML = await page.content()
  const fs = require('fs');
  var ws = fs.createWriteStream(
    'TempInterfaceWithChrome.js'
  );
  ws.write(HTML);
  ws.end();
  var ws2 = fs.createWriteStream(
    'finishedFlag'
  );
  ws2.end();
  browser.close();
})();
