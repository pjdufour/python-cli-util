import sys


def _run_task_core(task, args, kwargs):
    if task:
        if args:
            task(* args)
        elif kwargs:
            task(** kwargs)
        else:
            task()


def cron_command(f, user, command, filename):
    template = 'echo "{f} {u} {c}" > /etc/cron.d/{filename}'
    cmd = template.format(
        f=f,
        u=user,
        c=command,
        filename=filename)
    return cmd


def request_input(question, value, required, options=None):
    if value:
        return value
    else:

        if options:
            print question+" :"
            print "* Options Below."+("  Enter to skip." if not required else "")
            for opt in options:
                print "| -- "+opt
            print "* Select option:",
        else:
            print question+":",


        if required:
            value = None
            while not value:
                value = raw_input()
                if not value:
                    print "Value required.  Please try again.  Ctrl+C to cancel."
                    print question+":",
                elif options and (not value in options):
                    print "Must select one of the options.  Ctrl+C to cancel."
                    print question+":",
                    value = None
            return value

        else:
            while not value:
                value = raw_input()
                if not value:
                    return None
                elif options and (not value in options):
                    print "Must select one of the options.  Enter to skip.  Ctrl+C to cancel."
                    print question+":",
                    value = None
            return value


def request_continue():
    print "Continue (y/n)?",
    confirm = raw_input()
    return confirm and confirm.lower() == "y"
