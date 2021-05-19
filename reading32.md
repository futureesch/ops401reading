Reading 32

https://www.toolbox.com/it-security/data-security/articles/what-is-malware-analysis-definition-types-stages-best-practices/ 

Malware is “software designed to infiltrate or damage a computer system without the owner’s informed consent. Any software performing malicious actions, including information stealing, spying, etc., can be referred to as malware.” 

Malware analysis is “The process of dissecting malware to understand its core components and source code, investigating its characteristics, functionality, origin, and impact to mitigate the threat and prevent future occurrences.” 

Demystifying malware and cyberthreats to increase awareness.
Investigates its characteristics
It unravels its functionality
It traces the malware’s origin
It tries to predict the impact

Step 1: Capture the malware. 

Step 2: Build a malware lab. 

Step 3: Install your tools. 

Step 4: Record the baseline. 

Step 5: Commence your investigation. 

Step 6: Document the results. 

Malware analysis is at the heart of cybersecurity innovation today. Analysts can work with governments, non-profit organizations, research institutions, and corporates to develop the body of knowledge around malware.

1. Static malware analysis 
Malware code includes two types of elements — static and dynamic. This type of analysis focuses on the former, examining static properties like metadata, headers, embedded assets, etc. A quick static analysis often reveals enough information needed to create an indicator of compromise (IOC), a document recording the software’s malicious nature. In case the results of static analysis are optimistic, the code is usually discarded like a piece of bad programming, not meriting further investigation as malware. 

2. Dynamic malware analysis 
Dynamic analysis allows the malware to play itself out in a controlled environment while observing its behavior. VMs are critical when conducting dynamic analysis, as it is likely that the malware will cause irreparable damage to its host environment. 

Several behavioral signals require your attention during dynamic malware analysis — including its interactions with network traffic, its targeting patterns towards the file system, and any changes to the registry. 

3. Manual malware analysis 
In a manual analysis, an analyst may choose to break down the code manually, using tools like debuggers, decompilers, and decrypters. Manual analysis often reveals the strategic intent behind malicious software; because the analyst examines the core logic of the algorithm and tries to predict the logic behind elements that seem unnecessary at first appearance. 

Manual analysis is also known as code reversing since you are essentially beginning with the final software, moving backward into code, and then arriving at the original logic — instead of the other way around. 

4. Automated malware analysis 
Automated analysis passes the malware through an automated workflow where its different behavioral and static properties are tested. This may not provide insights into the software’s logic, but it is extremely useful for understanding its broader classification and to which malware family it might belong to. 

1. Observing malware behavior 
At the initial stages, malware analysts run tools or execute short, manual exercises to force it to react. Once the malware reacts to its surrounding environment (on a VM), it becomes easier to understand whether it is harmless or a potential threat. 

2. Disassembling the code 
Disassembling the code involves both static analysis — where you look at the unchangeable elements of the malware code — as well as its inner logic. Code disassembly relies on manual efforts to a large extent, which is why it is recommended that malware analysts bring some knowledge in binary and assembly language. You could also leverage a ready-to-use disassembler to tear down the malware program, converting the logic from an original binary form into assembly language. Typically, three types of tools can help at this stage: 

3. Examining the memory 
At this stage, we dive into the forensic artifacts left behind by the malware on your system’s memory. The average malware is often 1MB or less in size, so it is difficult to observe its memory imprint in everyday computing environments. A malware analysis lab provides the conditions necessary to benchmark the pre-malware memory state, run it, and then extract artifacts resulting from its functionalities. 

Memory analysis can be extremely difficult, as you are looking for the most minute of digital imprints left behind by an extremely light application designed for stealth. Fortunately, there are several tools out there to help at this stage, such as Memoryze, a free tool that analyzes memory images to list all running processes (including hidden ones), identify loaded drivers, verify driver signatures, and display any open network sockets. 


1. Expand your malware sample size continuously. 
2. Use automation to optimize your efforts. 
3. Always use a secure environment to run malware.
4. Only analyze malware whose remote infrastructure is running. 
5. Capture and store VM image snapshots.
6. Do your research and select the best-fit malware analysis tools.

Here are some of the tools to watch out for in 2020: 

CIRCL Dynamic Malware Analysis Platform (DMA) – a public service that lets you analyze malware in a controlled environment, securely upload sensitive documents, and perform advanced tasks like memory forensics
Dinoflux – a malware analysis platform that studies behavior uses reverse engineering techniques and creates comfortable indicators of compromise outcomes, integrating with your security operations center (SOC)
Sndbox – a malware research platform powered by artificial intelligence (AI) and advanced driver analysis, with an invisible agent that convinces the malware to reveal its full functionality
Even a casual glance at today’s cybersecurity landscape will reveal countless malware variants, and the number is growing exponentially with each passing day. It is estimated that over 350,000 new pieces of malicious code are identified every day. Understanding malware analysis, its stages, and best practices is essential for staying ahead and staying safe.
