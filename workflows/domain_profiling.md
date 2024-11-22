# Domain Profiling with Maltego

This workflow guides you through profiling a domain to uncover relationships and critical information.

## Steps
1. Start Maltego and create a new graph.
2. Add a "Domain" entity to the canvas.
3. Input the target domain (e.g., `example.com`).
4. Run the following transforms:
   - **To DNS Name**: Discover subdomains.
   - **To IP Address**: Identify associated IP addresses.
   - **To WHOIS Record**: Extract WHOIS information.
5. Analyze the graph for connections between entities.
6. Save and export the graph as a visual report.

## Example Output
![Domain Profiling Graph](../screenshots/graph_example1.png)

