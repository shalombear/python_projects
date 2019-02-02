# keyword match two strings

"""
function:
    kw_match -- analyze and compare keywords in two strings
        args:
            text1 (str)
            text2 (str)
        returns:
            report (str)
"""

# find the intersection, differences, symmetric differenc, and relevant metrics
def kw_match(text1, text2):
    """analyze and compare keywords in two strings
        args:
            text1 (str)
            text2 (str)
        returns:
            report (str)
    """
    break1 = text1.split("\n")
    break2 = text2.split("\n")

    list1 = []
    list2 = []
    for text in break1:
        list1.extend(text.split(" "))
    for text in break2:
        list2.extend(text.split(" "))

    

    set1 = set(list1)
    set2 = set(list2)

    set1.remove('')
    set2.remove('')
    

    return set1, set2


# begin test phase
text1 = """The Development Analyst I is responsible for advanced application development and enhancement to existing applications and scripts.

REQUIREMENTS

 

Determine barriers and formulate options or needs to meet development project goals. (Software, Access, Security, Network resources) 
Ability to document new and modified code in applications and scripts. 
Adhere to all standardizations and processes of the development team, including the approval process of all new project work. 
Develop in test environment and beta test with Champions and associates; receive feedback and make enhancements to operational needs. 
Understand upstream and downstream impacts to established processes mitigating process breaks.  
Collaborate with other scripting team members to ensure development and testing is on schedule 
Attend scheduled meetings for updates on current processes, projects, and barriers. 
Work with management and associate base looking for opportunities to leverage technology and reporting for efficiencies and productivity 
Lead successful design and completion of in house applications. 

EXPERIENCE



Knowledge of Python, and other languages as needed. 
Primary emphasis on VBA/VB, Python, C# development, helpful
Experience with Boston Workstation preferred. Macro Express a plus. 
Understanding of database development, data structures, relational databases. MSSQL 
Understand scheduled automated processes via Window Scheduler 
Ensure FTP (File Transfer Protocol) dependent processes are scheduled and reacted to if failed. 
Knowledge of host systems and interfaces between host and complimentary systems a plus. (Artiva, Recondo, Hyland, SSI, ESS, AS400 etc.) 
Knowledge of X12 Electronic Data Interchange. (EDI) 
Grasp of statistics, probability, general mathematics. 
Knowledge of developing in multiple Operating Systems including Windows, Linux.
Must have strong PC skillset and an understanding of networking principles.
Excellent debugging skillset for new application development and existing application and scripted process. 
Review current processes for enhancement moving manual processing to application, scripted, or macro driven processes. 
Create automated error reporting for all developed applications and scripts.
React to error report for debugging and documentation of root cause failure. 
Ensure all developed application and automation is HIPAA compliant."""

text2 = """Python, SQL, HTML, CSS, Linux, Windows, Bash, Git, LaTeX, MATLAB
Problem-solving, conceptual abstraction, strong mathematical and analytical skills
Machine learning, statistical analysis, algorithm design, mathematical modeling
MS Word, Excel, PowerPoint, Access
Adobe InDesign, Photoshop
Professional Experience

Data Scientist, Sholom Consulting
Construct, analyze, and refine mathematical models in various applied research areas
Collect and clean data and organize in relational databases and other file formats
Write algorithms in Python to aid in understanding, manipulating, and visualizing data
Time series analysis and linear modeling with Python pandas, sk-learn, and matplotlib
Designed tracking system to achieve 30% improvement in warehousing efficiency

Math Tutor, University of Cincinnati
Led study groups to help students understand material and prepare for exams
Ran collaborative problem-solving discussions and programming tutorials
Subjects included real analysis, linear algebra, group theory, formal logic, statistics

Membership Coordinator, IVAW
Oversaw threefold growth in organizational membership
Welcomed new members and onboarded them to organizational activities
Facilitated communication between regional coordinators, chapter leaders, working
groups, key personnel, and at-large membership.

Editor-in-Chief, Sit-Rep
Directed publishing cycle of news magazine by and for 21st Century veterans
Managed contributors’ bureau, guided voice and tone of publication, wrote copy
Edited, supervised design, layout, printing, and distribution

Social Media Content Creator, Chulent
Organized community events, blogged, conducted interviews, collated content
Scanned RSS feeds, analyzed data, consulted on technical and editorial matters

Research Assistant, Freelance
Discovered, analyzed, parsed, and translated historical texts, documents, and artifacts
Organized data, cataloged findings, analyzed metadata, wrote reports

Communications Technology Specialist, U.S. Army
Installed, operated, and maintained extension node in telecommunications network
Provided secured and unsecured telephone and internet service to multiple units
Provided customer service, technical support, and technological assistance
Maintained vehicle, generator, and signal equipment in hostile or inhospitable territory"""

set1, set2 = kw_match(text1, text2)
