import TEST_URL from './util.js'
import { Selector } from 'testcafe'

fixture `Getting Started`.page `${TEST_URL}/`

test (`should display the page`, async t => {
  const title = Selector('#title').withExactText('J Interpreter')
  await t.expect(title.exists).ok()

  })
