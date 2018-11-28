const puppeteer = require('puppeteer');
(async() => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setExtraHTTPHeaders({Referer: 'https://sparktoro.com/'}) 
  await page.goto('https://www.monetizemore.com', {waitUntil: 'networkidle2'});
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