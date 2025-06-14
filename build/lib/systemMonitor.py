import keyboard, psutil, time, sys, os, colorama
import argparse 

colorama.init()

def system(bunny, interval):
    # total characters per line, including the two '||' 
    TOTAL_WIDTH = 41  
    INNER_WIDTH = TOTAL_WIDTH - 4

    def bordered(line: str):
        # trim or pad to exactly INNER_WIDTH, then wrap
        return "|  " + line[:INNER_WIDTH].ljust(INNER_WIDTH) + "  |"
    
    if bunny:
        print(
        r"(\ /)" + r"                (\ /)" + "\n" \
        "( · ·)" + "              (· · ) " + "\n" \
        "c(')(')" + r"   \|/      (')(')ↄ" + r"    \|/"+"\n"
        )

        print(
            r"    (\ /)"+"\n" \
            "    (. .)\n" \
            "---˅-----˅---------------------------------"
        )
        
    else:
        print("-------------------------------------------")

    while True:
        # exit
        if keyboard.is_pressed('esc'):
            os.system('cls')
            break

        net1 = psutil.net_io_counters()
        time.sleep(interval)
        net2 = psutil.net_io_counters()

        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        bat = psutil.sensors_battery()
        plug = "(Plugged in)" if bat.power_plugged else "(Not Plugged in)"

        # uptime
        ups = int(time.time() - psutil.boot_time())
        days, rem = divmod(ups, 86400)
        hrs, rem = divmod(rem, 3600)
        mins, secs = divmod(rem, 60)

        # net speeds in Mbps
        down = (net2.bytes_recv - net1.bytes_recv)*8/interval/1e6
        up   = (net2.bytes_sent - net1.bytes_sent)*8/interval/1e6

        # build each line’s content, then pad & wrap
        lines = [
            f"CPU: {cpu:5.1f}% | RAM: {mem:5.1f}% | DISK: {disk:5.1f}%",
            f"Battery: {bat.percent:5.1f}% {plug}",
            "",  # blank line
            f"Uptime: {days}d {hrs:02d}:{mins:02d}:{secs:02d}",
            "",  # blank line
            f"Net Down: {down:6.2f} Mbps",
            f"Net   Up: {up:6.2f} Mbps"
        ]

        # print them all in one go
        for ln in lines:
            sys.stdout.write(bordered(ln) + "\n")
        sys.stdout.write("-------------------------------------------")
        sys.stdout.flush()

        # move cursor back up so next frame overwrites exactly the same block:
        sys.stdout.write(f"\033[{len(lines)}F")

    return

def main():
    parser = argparse.ArgumentParser(
        prog="hopmon",
        description="Real-time terminal system monitor with little bunny splash"
    )

    parser.add_argument(
        "-i", "--interval",
        type=float,
        default=0.5,
        help="Seconds between updates (default 0.5)"
    )

    parser.add_argument(
        "-b", "--bunny",
        action="store_true",
        help="Toggle little bunny splash"
    )

    args = parser.parse_args()
    system(bunny=args.bunny, interval=args.interval)

if __name__ == "__main__":
    main()