# Blockchain Hackathon

For this hackathon, we will ask you to fill in some template code to create  blockchain-based crowdfunding application by leveraging smart contracts

## Project Breakdown
A crowdfunding DApp helps eliminate the trust basis required between a donor and a 3rd party individual collecting these donations. Implementing a decentralized application lifts the extra processing fees and margins allocated by 3rd party organizations; with DApps the only additional cost comes from gas fees. The goal of this exercise will be to develop a simple decentralized app that provides the same functionalities as any other standard crowdfunding platform, but with the ability to deploy the application onto a blockchain and pay using Ether.

## Actionable Steps
1. Define a function to fund a project 
    * Require that the address of the sender does not equal the creator of the project 
    * Store the contributions of the sender and update the existing balance 
    * Emit an event stating that funding has been received with sender, value and the balance 
    * Finally check if the funding is complete or expired
2. Define a function to check if funding is complete or expired 
    * If the current balance is greater than the goal amount, then pay out and change the state to successful 
    * If the date is greater than the expiry date then change the state to expired
    * Define a function to give the received funding to the project starter 
    * Define a function to retrieve donated amount if a project expires
3. Define a function to give the received funding to the project starter
4. Define a function to retrieve donated amount if a project expires

## How to begin

1. Copy the link below:
```

https://github.com/mustafa-tariqk/qmind-workshop/blob/main/Hackathon/Crowdfunding.sol

```

2. Go to the site linked below:

https://remix.ethereum.org/

3. You should be in the Remix editor with a general home tab welcoming you in the middle, a directory in the left column and some sort of terminal in the bottom. Below the `Featured Plugins` and `File` sections, you will see a row of buttons under `Load From` that say `Gist`, `GitHub`, and more. Click the `GitHub` option.

4. Paste the link you copied in part 1 into the window that popped up.

5. Click `OK`.

6. Cick that `github` folder, then click `mustafa-tariqk`, and then open `Auction.sol`.

7. And you are done! Fill it out and submit it to us when you're done!
