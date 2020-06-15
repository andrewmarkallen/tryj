import TEST_URL from './util.js'
import { Selector } from 'testcafe'

fixture `Console`.page `${TEST_URL}`

test (`Console should appear`, async t => {

  const jconsole = Selector('.react-console-container')
  await t.click(jconsole)
        .typeText(jconsole, 'woof')
        .expect(jconsole.withText('woof').exists).ok()
  })

test (`Console should execute code`, async t => {

  const jconsole = Selector('.react-console-container')
  await t.click(jconsole)
        .typeText(jconsole, '+/\\ i.10')
        .expect(jconsole.withText('0 1 3 6 10 15 21 28 36 45').exists).ok()
  })
