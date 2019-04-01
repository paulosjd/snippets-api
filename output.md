**Async: a style of concurrent programming in which tasks release the CPU during
waiting periods, so other tasks can use it**


3 ways of doing multiple things at once in Python: multiprocessing,
multithreading, asynchronous programming

**Multiprocessing and multithreading**
Concurrency is when two or more tasks can start, run, and complete in
overlapping time periods. It doesn't necessarily mean they'll ever both be
running at the same instant. Eg. multitasking on a single-core machine.
Parallelism is when two or more tasks  run at the same time, e.g. on a multicore
processor. Concurrency can be characterized as a property of a program or system
and parallelism as the runtime behaviour of executing multiple tasks at the same
time.

![](images/concurrency_parallelism.png)
If we ran this program on a computer
with a single CPU core, the OS would be switching between the two threads,
allowing one thread to run at a time. If we ran this program on a computer with
a multi-core CPU then we would be able to run the two threads in parallel - side
by side at the exact same time

A thread is a sequence of instructions within a
process. It can be thought of as a lightweight process. Threads share the same
memory space. A process is an instance of a program running in a computer which
can contain one or more threads. A process has its independant memory space.
The threading module is used for working with threads in Python. The CPython
implementation has a Global Interpreter Lock (GIL) which allows only one thread
to be active in the interpreter at once. The mechanism used by the CPython
interpreter to assure that only one thread executes Python bytecode at a time.
This simplifies the CPython implementation by making the object model (including
critical built-in types such as dict) implicitly safe against concurrent access.
Locking the entire interpreter makes it easier for the interpreter to be multi-
threaded, at the expense of much of the parallelism afforded by multi-processor
machines. This means that threads cannot be used for parallel execution of
Python code. While parallel CPU computation is not possible, parallel IO
operations are possible using threads. This is because performing IO operations
releases the GIL. What are threads used for in Python? 

    In GUI applications
to keep the UI thread responsive

    IO tasks (network IO or filesystem IO)
Using threads for these tasks improves performance, since in network IO for
example, most of the time is spent waiting for a response from the URL. Threads
should not be used for CPU bound tasks as this will actually result in worse
performance compared to using a single thread.

For parallel execution of tasks
use multiprocessing, a package that supports spawning processes using an API
similar to the threading module. It side-steps the GIL by using subprocesses
instead of threads. The Pool object which offers a convenient means of
parallelizing the execution of a function across multiple input values,
distributing the input data across processes (data parallelism).

**Using
coroutines to run functions concurrently**

While threads are useful for
blocking I/O, they should be avoided for parallel procesessing. Three problems
with threads: special tools are needed e.g. to prevent data races, which
increases code complexity and difficultly with its maintenance, and executing
threads requires uses a lot of memory and are costly to start. 

Python work
around these rpoblem with coroutines. These allow you to have many seemingly
simultaneous functions running in your programs. They are are extension of
generators and the cost of starting them is just a function call and require
only a small amount of memory until they are exhausted.

Again, how does Python do multiple things at once?

1 - Multiple processes

The
most obvious way is to use multiple processes. From the terminal you can start
your script two, three, four…ten times and then all the scripts are going to run
independently or at the same time. The operating system that's underneath will
take care of sharing your CPU resources among all those instances. Using CPython
that's actually the only way you can get to use more than one CPU at the same
time.

2 - Multiple threads

The next way to run multiple things at once is to
use threads.

A thread is a line of execution, pretty much like a process, but
you can have multiple threads in the context of one process and they all share
access to common resources. But because of this it's difficult to write a
threading code. And again, the operating system is doing all the heavy lifting
on sharing the CPU, but the global interpreter lock (GIL) allows only one thread
to run Python code at a given time even when you have multiple threads running
code. So, In CPython, the GIL prevents multi core concurrency. Basically, you’re
running in a single core even though you may have two or four or more.

3 -
Asynchronous Programming

The third way is an asynchronous programming, where
the OS is not participating. As far as OS is concerned you're going to have one
process and there's going to be a single thread within that process, but you'll
be able to do multiple things at once. So, what's the trick? 

Much of the code
we write, especially in heavy IO applications like websites, depends on external
resources. This could be anything from a remote database call to POSTing to a
REST service. As soon as you ask for any of these resources, your code is
waiting around with nothing to do. With asynchronous programming, you allow your
code to handle other tasks while waiting for these other resources to respond.

Coroutines: a background
-------------------------

Coroutines have similarities
to generators. When you call a generator function, a generator object is
returned. The function is not run, it only executes on `next()`. Yield produces
a value but the function is suspended and resumes on the next call to `next()`
until StopIteration is reached.

```python
# Generators generate data, coroutines consume data. You can advance a generator to the yield statement by the 
# send method, however sending anything other than `None` to a generator causes an Exception to be raised.
def my_gen():
    # a generator function yielding even numbers < 10
    for i in range(10):
        if i % 2 == 0:
            yield i
        
g = my_gen()
data = [g.send(None) for i in range(5)] 
assert data == list(my_gen()) 
data 
```

Following PEP-342, you can use `yield` in expressions, such as the RHS of
assignments. If you use `yield` more generally, you get a coroutine. These do
more than generate values, they can consume values sent to them (you can only
send None to a generator, effectively the same as calling `next()` on it).
Values sent to them are returned by (yield):

```python
def grep(pattern):
    print ("Looking for {}".format(pattern))
    while True:        
        line = (yield)       
        if pattern in line:            
            print(line)
            
g = grep('Python')
next(g)
```

Execution is similar as for generators. 'Priming' the coroutine by calling
`next()` or `.send(None)` advances the coroutine to the first `yield` and
execution is suspended until it is sent a value.

```python
g.send('no snakes here')
g.send('Python, you are so cool')
g.close()
```

The need to call `next()` can be solved using a decorator :

```python
def coroutine(func):    
    def start(*args,**kwargs):        
        cr = func(*args,**kwargs)        
        next(cr)        
        return cr    
    return start
```

**Processing Pipelines**

Coroutines can be used to set up pipes. The source
(typically not a coroutine) drives the pipeline.You just chain coroutines
together and push data through the pipe with `send()` operations
![](images/proc_pipeline.png)

async/await
----------

```python
import asyncio

async def speak_async():  
    print('OMG asynchronicity!')

# cannot run with something driving it
speak = speak_async()
speak
```

```python
speak.send(None)
```

```python
async def run_this():
    await speak_async()

# Blocking call which returns when the display_date() coroutine is done
loop.run_until_complete(run_this())
```

```python
import asyncio

loop = asyncio.get_event_loop()

async def hello():
    print('Hello')
    await asyncio.sleep(3)
    print('World!')  
  
loop.run_until_complete(hello())
```

**How is Async implemented**

A practical definition of Async is that it's a
style of concurrent programming in which tasks release the CPU during waiting
periods, so that other tasks can use it. How can you do that with one process
and one thread? You need two things, basically.

The first thing that you need
is to have a function that can suspend and resume. A function that enters a
waiting period is suspended, and only resumed when the wait is over. This can be
done using async/await keywords that you can use in Python 3.5+.

The next thing
that we need is a piece of code that can decide how the CPU is shared, which
function gets the CPU next. So, we need a scheduler of sorts. And in
asynchronous programming this is called an event loop.

**Scheduling
Asynchronous Tasks**

An event loop will know all the tasks that are running or
want to run, it'll select one and give control to it. That task is going to
suspend when it needs to wait for something. The control will go back to the
loop and the last will find another task and it'll keep going that way. This is
called cooperative multi-tasking. Let's say that we wanna write a little script
that prints 'hello' waits 3 seconds and then prints 'world'.

```python
from time import sleep

def hello():
    print('Hello')
    sleep(3)
    print('World!')
    
for i in range(2):
    hello()
```

If we were to put a loop on that 'hello' on the bottom to run 'hello' 10 times,
for example, this is gonna run not for 3 seconds but for 30 seconds. 

In this
next example we're using a generator function. The nice thing about them is that
you don't have to pre-generate all the entire sequence you can generate elements
of that sequence as the person calling the generator asks. You can repurpose
that using yield or yield from keywords and also use it for an asynchronous
function. Basically, when we reach the yield from in the example above, we are
saying: "OK, loop, I'm done for now, so I give you back control. Please, run
this function for me [the one that follows the yield from], so asyncio sleep for
3 seconds. And when that's done I'm ready to continue". The loop will take note
of that and then manage everything. Because it’s a scheduler and that's what it
does. So, if you were to call this 'hello' function 10 times instead of running
for 30 seconds you're gonna see 10 hellos then a pause for 3 seconds and then
you’re gonna see 10 'worlds'.

```python
asyncio.set_event_loop(asyncio.new_event_loop())

import asyncio
import datetime

async def display_date(loop):
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

loop = asyncio.get_event_loop()
# Blocking call which returns when the display_date() coroutine is done
loop.run_until_complete(display_date(loop))
loop.close()
```

The one of the things that asyncio is great for is that it makes very explicit
the points where the code suspends and resumes.

**Example: Chain Coroutines**

```python
asyncio.set_event_loop(asyncio.new_event_loop())

async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)
    return x + y

async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))

loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(1, 2))
loop.close()
```

`compute()` is chained to `print_sum()` meaning that `print_sum()` coroutine
waits until `compute()` is completed before returning its result.

Sequence
diagram of the example:

![](images/tulip_coro.png)

**Event loop is closed exception**

You have already called loop.close() before
you ran that sample piece of code, on the global event loop, so you need to
create a new loop:

loop = asyncio.new_event_loop()

You can set that as the new
global loop with:

asyncio.set_event_loop(asyncio.new_event_loop())

and then
just use asyncio.get_event_loop() again.

Alternatively, just restart your
Python interpreter, the first time you try to get the global event loop you get
a fresh new one, unclosed.

Asynchronous HTTP requests in Python
-------------------------------------

You
can consider aiohttp as the asynchronous version of requests. Usage is very
similar to requests but the  performance benefits can be huge. If you haven’t
used the NBA’s statistics API you should know that it can be extremely slow.
Calls can take upwards of 5-6 seconds and collecting data from the API can be
major pain.

```python
#Approx. 12 minutes!

import requests

base_url = 'http://stats.nba.com/stats'
HEADERS = {
    'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/45.0.2454.101 Safari/537.36'),
}


def get_players(player_args):
    endpoint = '/commonallplayers'
    params = {'leagueid': '00', 'season': '2016-17', 'isonlycurrentseason': '1'}
    url = '{}{}'.format(base_url, endpoint)
    print('Getting all players...')
    resp = requests.get(url, headers=HEADERS, params=params)
    data = resp.json()
    player_args.extend(
        [(item[0], item[2]) for item in data['resultSets'][0]['rowSet']])


def get_player(player_id, player_name):
    endpoint = '/commonplayerinfo'
    params = {'playerid': player_id}
    url = '{}{}'.format(base_url, endpoint)
    print('Getting player {}'.format(player_name))
    resp = requests.get(url, headers=HEADERS, params=params)
    print(resp)
    data = resp.text
    with open('{}.json'.format(player_name.replace(" ", "_")), 'w') as file:
        file.write(data)


player_args = []
get_players(player_args)
#for args in player_args:
#    get_player(*args)
print('this would take 12 mins!')
```

After gathering the player ID’s and player names the program synchronously
gathers player information and stores it in files with the format
FIRSTNAME_LASTNAME.json.
It’s a fairly straightforward program and takes around
12 minutes of total time. The following asychronous way is far quicker:

```python
import asyncio
import aiofiles
import aiohttp

base_url = 'http://stats.nba.com/stats'
HEADERS = {
    'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/45.0.2454.101 Safari/537.36'),
}

async def get_players(player_args):
    endpoint = '/commonallplayers'
    params = {'leagueid': '00', 'season': '2016-17', 'isonlycurrentseason': '1'}
    url = '{}{}'.format(base_url, endpoint)
    print('Getting all players...')
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=HEADERS, params=params) as resp:
            data = await resp.json()
    player_args.extend(
        [(item[0], item[2]) for item in data['resultSets'][0]['rowSet']])

async def get_player(player_id, player_name):
    endpoint = '/commonplayerinfo'
    params = {'playerid': player_id}
    url = '{}{}'.format(base_url, endpoint)
    print('Getting player {}'.format(player_name))
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=HEADERS, params=params) as resp:
            print(resp)
            data = await resp.text()
    async with aiofiles.open('{}.json'.format(player_name.replace(" ", "_")), 'w') as file:
        await file.write(data)

loop = asyncio.get_event_loop()
player_args = []
loop.run_until_complete(get_players(player_args))
loop.run_until_complete(
    asyncio.gather(
        *(get_player(*args) for args in player_args)
    )
)
```
