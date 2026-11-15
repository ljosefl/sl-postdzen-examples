using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

namespace modular_monolith
{
    public class Program
    {
        public static void Main(string[] args)
        {
            CreateHostBuilder(args).Build().Run();
        }

        public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureServices((hostContext, services) =>
                {
                    services.AddServiceFabric();
                    services.AddModularMonolith();
                })
                .UseServiceFabricHosting();
    }
}

namespace modular_monolith
{
    public static class ServiceFabricExtensions
    {
        public static IHostBuilder AddServiceFabric(this IHostBuilder builder)
        {
            // Фиктивная реализация
            return builder;
        }

        public static IHostBuilder AddModularMonolith(this IHostBuilder builder)
        {
            // Фиктивная реализация
            return builder;
        }

        public static IHostBuilder UseServiceFabricHosting(this IHostBuilder builder)
        {
            // Фиктивная реализация
            return builder;
        }
    }
}