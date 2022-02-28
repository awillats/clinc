| Expt.                | Causal                                 |
| -------------------- | -------------------------------------- |
| observe              | correlations                           |
| condition            | adjusting, partial correlations        |
| perturb              | x+= val, instrumental variables?       |
| ↪ sweep input        | x+= $∀v \in {\text{values}}$           |
| clamp                | $\text{do}(x⇐\text{val})$              |
| ↪ lesion             | $\text{do}(x⇐\empty)$                  |
| ↪ sweep output[^ACE] | $\text{do}(x⇐∀v \in {\text{values}} )$ |

[^ACE]: see also [average causal effect](https://en.wikipedia.org/wiki/Average_treatment_effect). something like $ \mathbb{E}[y | do(x⇐1)] - \mathbb{E}[y | do(x⇐0)]$
