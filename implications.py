from ice.recipe import recipe 

def make_substatement_prompt(statement: str) -> str:
    return f"""Decompose the following statement into 2-5 implications that would help you break down the assertion. Make the statements stand alone, so that they can be asserted without the context of the original statement.


 Statement: "{statement}"
 Substatements:
-""".strip()

async def assert_implications(
    statement: str = "Bob murdered Alice on the 25th of June at the Rogers Estate with arsenic.",
):
    prompt = make_substatement_prompt(statement)
    substatements_text = await recipe.agent().complete(prompt=prompt)
    substatements = [line.strip("- ") for line in substatements_text.split("\n")]
    return substatements


recipe.main(assert_implications)