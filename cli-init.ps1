function procmanager {
    $action = $args[0]
    $proc = $args[1]
    py C:\Code\Python\process-manager\main.py $action $proc
}