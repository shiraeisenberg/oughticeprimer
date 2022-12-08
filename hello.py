from ice.recipe import recipe


async def test_function(num1,num2):
    return 

async def say_hello():
    result = await test_function(1,2)
    return "Hello world!"


recipe.main(say_hello)