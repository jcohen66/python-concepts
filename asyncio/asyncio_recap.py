import asyncio
from random import randint
from time import perf_counter
from typing import AsyncIterable

from req_http import JSONObject, http_get, http_get_sync

# The highest Pokemon id
MAX_POKEMON = 898


def get_random_pokemon_name_sync() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = http_get_sync(pokemon_url)
    return str(pokemon["name"])


async def get_random_pokemon_name() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = await http_get(pokemon_url)
    return str(pokemon["name"])


async def get_pokemon() -> JSONObject:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = await http_get(pokemon_url)
    return str(pokemon["name"])


async def next_pokemon(total: int) -> AsyncIterable[str]:
    for _ in range(total):
        name = await get_random_pokemon_name()
        yield name


async def main() -> None:
    time_before = perf_counter()
    for _ in range(20):
        pokemon_name = await get_random_pokemon_name()
        print(pokemon_name)
    print(f"Time (sync): {perf_counter() - time_before}")

    time_before = perf_counter()
    result = await asyncio.gather(*[get_random_pokemon_name() for _ in range(20)])
    print(result)
    print(f"Time (async): {perf_counter() - time_before}")

    time_before = perf_counter()
    async for name in next_pokemon(20):
        print(name)
    print(f"Time (gen sync): {perf_counter() - time_before}")

    time_before = perf_counter()
    names = [name async for name in next_pokemon(20)]
    print(names)
    print(f"Time (gen async): {perf_counter() - time_before}")


if __name__ == "__main__":
    asyncio.run(main())
