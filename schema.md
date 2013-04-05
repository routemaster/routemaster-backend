# Database Collections

## `users`

*   `uid` (integer)
*   `name` (string)
*   `registerDate` (date)
*   `lastLoginTime` (datetime)
*   `distance` (integer)
*   `exploration` (integer)

## `routes`

*   `rid` (integer)
*   `uid` (integer)
*   `pid` (integer, optional)
*   `date` (date)
*   `start_wid` (integer)
*   `end_wid` (integer)
*   `distance` (integer, in meters)
*   `disqualified` (boolean)
*   `efficiency` (integer, 0–100)
*   `time` (integer, in seconds)

## `waypoints`

*   `wid` (integer)
*   `uid` (integer)
*   `rid` (integer)
*   `name` (string)
*   `date` (date)
*   `position` (pair of floats?)
*   `accuracy` (integer?)

## `popularpaths`

*   `pid` (integer)
*   `wids` (list of integers)

## `sessions`

*   `uid` (integer)
*   `uuid` (string?)
*   `time` (datetime)
