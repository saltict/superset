# Custom CSS 
### For responsive

```
@media only screen and (max-width: 600px) {
  .dashboard-content  > div:not(.grid-container):not(.dashboard-builder-sidepane) {
    display: none;
  }
  
  .dashboard-content > .grid-container {
    margin: 16px;
  }
  
  .dashboard-header {
    padding-left: 16px;
    padding-right: 16px;
  }
  
  .dashboard-component-header {
    padding-top: 8px;
    padding-bottom: 8px;
  }
}

```


### For remove header
```
#app-menu {
  display: none;
}
```
