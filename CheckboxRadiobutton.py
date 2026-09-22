
#Checkbox

page.get_by_role("checkbox").first.uncheck()
expect(page.get_by_role("checkbox").first).not_to_be_checked()



#Radio Button

#Indexing starts with 0 so 3rd radio button will be nth(2)

page.get_by_role("radio").first.check()
expect(page.get_by_role("radio").first).to_be_checked()

page.get_by_role("radio").nth(2).check()
expect(page.get_by_role("radio").first).not_to_be_checked()
expect(page.get_by_role("radio").nth(2)).to_be_checked()