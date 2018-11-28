    const puppeteer = require('puppeteer');
    (async () => {
      const browser = await puppeteer.launch();
      const page = await browser.newPage();
      await page.setExtraHTTPHeaders({Referer: 'https://sparktoro.com/'}) 
      await page.goto('https://sparktoro.com/trending');
      await page.waitForSelector('div.title > a');
      const stories = await page.evaluate(() => {
      const links = Array.from(document.querySelectorAll('div.title > a'))
      return links.map(link => link.href).slice(0, 10)
      })
        console.log(stories);
        await browser.close();
        })();