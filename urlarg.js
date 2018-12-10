// Usage: node urlarg.js httpswebsite filename.html
const puppeteer = require('puppeteer');
const url = process.argv[2];
const filenameko = process.argv[3];
if (!url) {
    throw "Please provide URL as a first argument";
}
async function run () {
  const browser = await puppeteer.launch({args: ['--no-sandbox', '--disable-setuid-sandbox']});
  const page = await browser.newPage();
  await page.setExtraHTTPHeaders({Referer: 'https://google.com/'})
  await page.goto(url,{waitUntil: 'networkidle2'});
  var HTML = await page.content()
  const fs = require('fs');
  var ws = fs.createWriteStream(filenameko);
  ws.write(HTML);
  ws.end();
  var ws2 = fs.createWriteStream('finishedFlag');
  ws2.end();
  browser.close();
}
run();
