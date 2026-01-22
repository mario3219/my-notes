```
%q är y axeln i data, t är x axeln i data

[up,lo] = envelope(q,20,'peak');
hold on
plot(t,q,t,up,'linewidth',1.5)
legend('Signal','Envelope'), title('Magnetic Field Frequency Spectrum')
hold off
```