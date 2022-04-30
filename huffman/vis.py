
import heartrate; heartrate.trace(browser=True)

from heartrate import trace, files

trace(files=files.path_contains('.py'))
