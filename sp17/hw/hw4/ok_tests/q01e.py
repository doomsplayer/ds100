test = {
  'name': 'Question 1e',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> connection.execute(query_q1e).fetchall() == [('TED CRUZ FOR SENATE', 'CRUZ FOR PRESIDENT', 250012),('MAKE DC LISTEN', 'CRUZ FOR PRESIDENT', 30619),('DALLAS ENTREPRENEUR POLITICAL ACTION COMMITTEE', 'CRUZ FOR PRESIDENT', 20000),('THE FARM CREDIT COUNCIL POLITICAL ACTION COMMITTEE', 'MARCO RUBIO FOR PRESIDENT', 17500),('NISOURCE INC. PAC', 'KASICH FOR AMERICA INC', 15000),('THE SENATE VICTORY FUND PAC', 'DONALD J. TRUMP FOR PRESIDENT, INC.', 15000),('CABLEVISION SYSTEMS CORPORATION POLITICAL ACTION COMMITTEE', 'HILLARY FOR AMERICA', 15000),('A WHOLE LOT OF PEOPLE FOR GRIJALVA CONGRESSIONAL COMMITTEE', 'DONALD J. TRUMP FOR PRESIDENT, INC.', 14909),('OHIO NATIONAL FINANCIAL SERVICES POLITICAL ACTION COMMITTEE', 'KASICH FOR AMERICA INC', 12400),("EMILY'S LIST", 'HILLARY FOR AMERICA', 10000),('FUELCELL ENERGY PAC', 'HILLARY FOR AMERICA', 10000),('OCEANS PAC', 'HILLARY FOR AMERICA', 10000),('INVESTMENT COMPANY INSTITUTE POLITICAL ACTION COMMITTEE', 'MARCO RUBIO FOR PRESIDENT', 10000),('ALVAREZ & MARSAL HOLDINGS, LLC PAC', 'JEB 2016, INC.', 10000),('TRI-STATE MAXED-OUT WOMEN', 'HILLARY FOR AMERICA', 10000),('WINE INSTITUTE PAC', 'HILLARY FOR AMERICA', 10000),('BUCKEYE PATRIOT POLITICAL ACTION COMMITTEE', 'KASICH FOR AMERICA INC', 10000),('MIDWEST VALUES PAC', 'HILLARY FOR AMERICA', 10000),('KIDSPAC', 'HILLARY FOR AMERICA', 10000),('JOBS, OPPORTUNITIES AND EDUCATION PAC (JOE-PAC)', 'HILLARY FOR AMERICA', 10000)]
          True                                                                       
                      """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
