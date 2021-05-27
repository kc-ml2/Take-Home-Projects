## Approximating the Optimal Value Function

Consider a finite MDP $\mathcal{M} =(\mathcal{S},\mathcal{A},P,R,\gamma)$. where  $\mathcal{S}$ is the state space, $\mathcal{A}$  action space, $\mathcal{T}$  transition probabilities,  $\mathcal{R}$ reward fucntion, $\mathcal{r}$ the discount factor.
Define ${Q}^*$ to be the optimal state-action value $Q^*(s,a)= Q_{\pi^*}(s,a)$  where $\pi^*$ is the optimal policy. Assume we have an estimate $\tilde{Q}$ of $Q^*$, and $\tilde{Q}$ is bounded by $l_\infty$ norm as follows:

$${\parallel\tilde{Q}-Q^*\parallel}_\infty \le\varepsilon$$

where ${\parallel{x}\parallel}_\infty = {\mathcal{max}}_{s,a}\left\vert {x(s,a)} \right\vert$.

Assume that we are following the greedy policy with respect to $\tilde{Q}$, $\pi(s) = argmax_{a\in \mathcal{A}}\tilde{Q}(s,a)$. We want to show that the following holds: 

$${V_\pi(s)}\ge\ {V^*(s)}  -{2\varepsilon \over 1-\gamma } $$

Where ${V_\pi(s)}$ is the value function of the greedy policy $\pi$ and  ${V^*(s)}= max_{a\in \mathcal{A}}{Q^*}(s,a)$ is the optimal value function. 
This shows that if we compute and approximately optimal state-action value function and then extract the greedy policy for that approximate state-action value function, the resulting policy still does well in the real MDP. 

**Q1 )** Let $\pi^*$ be the optimal policy, $V^*$ the optimal value function and as defined above  $\pi(s) = argmax_{a\in \mathcal{A}}\tilde{Q}(s,a)$. Show the following bound holds for all states $s \in S$.

$${V^*(s)}-{Q^*}(s,\pi(s)) \le 2
\varepsilon$$

**Q2)** Using the result of Q1, prove that ${V_\pi(s)}\ge\ {V^*(s)} -{2\varepsilon \over 1-\gamma }$.
