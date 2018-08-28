import demo

def main(): 
  ## DATE RANGE DEMO
  # converts time to epoch and retrieves data for a hardcoded module
  start = demo.parseTime("2018 08 28 08 00 PST")
  end = demo.parseTime("2018 08 28 09 00 PST")
  demo.dateRange(start, end)

if __name__ == "__main__":
  main()
